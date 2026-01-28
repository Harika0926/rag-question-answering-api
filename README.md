# RAG-Based Question Answering System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based Question Answering API.
Users can upload documents and ask questions, and the system retrieves relevant content
from the documents before generating an answer using a Large Language Model.

## Tech Stack
- FastAPI
- FAISS (Vector Store)
- Sentence Transformers (Embeddings)
- Background Tasks for ingestion
- Pydantic for request validation

## Features
- Upload documents (PDF, TXT)
- Chunk and embed documents
- Store embeddings in FAISS
- Retrieve relevant chunks using similarity search
- Generate answers using an LLM
- Basic rate limiting

## Chunking Strategy
Documents are split into chunks of 500 tokens with 100 token overlap.
This balances semantic completeness and retrieval accuracy while preventing context loss.

## Metrics Tracked
Latency was tracked to measure retrieval and response generation time.

## Known Limitation
Vague or generic queries may retrieve less relevant chunks, impacting answer quality.

## Setup
1. Install dependencies:
   pip install -r requirements.txt
2. Run the API:
   uvicorn app.main:app --reload
