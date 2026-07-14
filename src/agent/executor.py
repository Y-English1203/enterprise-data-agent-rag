"""
RAG Retriever Module - Inspired by FastGPT's hybrid search strategy
Combines Vector Search (Chroma) + Keyword Search (BM25) for better recall.
"""

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from rank_bm25 import BM25Okapi
import numpy as np

class HybridRetriever:
    """
    Implements hybrid retrieval: Vector + Keyword (BM25)
    Designed to improve recall for domain-specific terms (e.g., "RFM", "LTV").
    """
    
    def __init__(self, persist_directory="./chroma_data"):
        self.embeddings = OpenAIEmbeddings()
        self.vector_db = Chroma(
            embedding_function=self.embeddings,
            persist_directory=persist_directory
        )
        # We'll load documents later for BM25
        self.documents = []
        self.bm25 = None
    
    def add_documents(self, docs: list[str]):
        """Add documents to both vector store and BM25 index."""
        self.vector_db.add_texts(docs)
        self.documents = docs
        # Tokenize for BM25
        tokenized_docs = [doc.lower().split() for doc in docs]
        self.bm25 = BM25Okapi(tokenized_docs)
    
    def retrieve(self, query: str, k: int = 5) -> list[str]:
        """
        Retrieve top-k documents using hybrid search.
        Combines vector similarity and BM25 keyword matching.
        """
        if not self.bm25:
            raise ValueError("No documents added. Call add_documents() first.")
        
        # Vector search
        vector_results = self.vector_db.similarity_search(query, k=k)
        vector_scores = self.vector_db.similarity_search_with_score(query, k=k)
        vector_scores = {doc.page_content: score for doc, score in vector_scores}
        
        # BM25 search
        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        top_bm25_indices = np.argsort(bm25_scores)[-k:][::-1]
        bm25_results = [self.documents[i] for i in top_bm25_indices]
        
        # Fusion: simple weighted sum (can be improved)
        combined = {}
        for doc in vector_results:
            combined[doc.page_content] = combined.get(doc.page_content, 0) + 0.7  # weight vector
        for doc in bm25_results:
            combined[doc] = combined.get(doc, 0) + 0.3  # weight bm25
        
        # Sort by score
        sorted_results = sorted(combined.items(), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in sorted_results[:k]]

# Example usage
if __name__ == "__main__":
    retriever = HybridRetriever()
    sample_docs = [
        "RFM analysis helps segment customers based on Recency, Frequency, Monetary value.",
        "LTV (Lifetime Value) is calculated as average purchase value * purchase frequency * customer lifespan.",
        "Churn rate is the percentage of customers who stop using a service over a period."
    ]
    retriever.add_documents(sample_docs)
    results = retriever.retrieve("How to calculate customer value?")
    print("Hybrid Retrieval Results:")
    for r in results:
        print("-", r)
