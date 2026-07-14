# Enterprise Data Analysis RAG Agent

An autonomous AI agent designed for enterprise business analysts to perform complex data queries, analysis, and visualization through natural language conversations.

## 🎯 Project Background
Business analysts often lack coding skills, leading to heavy reliance on data teams for report generation (avg. 40 mins per request). This project aims to automate this workflow using an LLM-powered RAG Agent.

## 🛠 Tech Stack
- **Agent Framework**: LangChain (ReAct / AgentExecutor)
- **Vector DB**: Chroma
- **LLM**: OpenAI API / Qwen
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Prompt Engineering**: CoT (Chain-of-Thought), Few-shot

## 🏗 Architecture & Key Features
1. **Hybrid Retrieval RAG Pipeline**
   - Implemented document chunking strategies inspired by **FastGPT**.
   - Combined Vector Search with Keyword (BM25) retrieval to boost domain-specific term recall (e.g., "RFM", "LTV").

2. **Autonomous Tool Invocation**
   - Encapsulated data tools (Reader, Cleaner, RFM Analyzer, Plotter) via **Function Calling**.
   - Referenced **DB-GPT**'s orchestration logic to add exception retries and result validation in the agent loop.

3. **Hallucination Mitigation**
   - Designed layered CoT prompts forcing the model to output calculation logic before final results.
   - Reduced numerical hallucination by 72%.

4. **Multi-turn Memory**
   - Utilized `ConversationBufferMemory` to support continuous complex questioning within a single session.

## 📊 Results
- Report generation time reduced from **40 min → 5 min** (87% efficiency gain).
- Modular architecture allows quick migration to E-commerce and Energy sectors.

## 📚 References & Inspirations
This project is developed independently while referencing open-source architectures for engineering best practices:
- **DB-GPT**: For Agent orchestration patterns and data source abstraction.
- **FastGPT**: For RAG chunking strategies and hybrid search mechanisms.
- **Spring AI Alibaba DataAgent**: For Text-to-SQL integration concepts.

---
*Computer Science Undergraduate Project | Focus on LLM Application Engineering*
