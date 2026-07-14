"""
Configuration Module - Centralized settings for the project.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    
    # Database
    CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_data")
    
    # Agent Settings
    AGENT_MAX_ITERATIONS = int(os.getenv("AGENT_MAX_ITERATIONS", 10))
    AGENT_TEMPERATURE = float(os.getenv("AGENT_TEMPERATURE", 0.0))
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Validate required keys
if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY == "your-api-key-here":
    raise ValueError("Please set OPENAI_API_KEY in .env file.")

# Example usage
if __name__ == "__main__":
    print("Config loaded:")
    print(f"API Key: {Config.OPENAI_API_KEY[:10]}...")
    print(f"Chroma Dir: {Config.CHROMA_PERSIST_DIR}")
