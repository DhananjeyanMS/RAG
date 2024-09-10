# RAG Project - Retrieval-Augmented Generation for Document-Based QA

This project implements a simple Retrieval-Augmented Generation (RAG) system that answers questions based on the contents of PDF and DOCX documents. It uses **Flask** for the web application, **Langchain** for text processing and handling of Large Language Models (LLMs), and **FAISS** for efficient vector-based similarity search.

## Project Overview

The RAG system works as follows:

1. **Document Reading**: The system reads multiple file types (PDF and DOCX) and combines their content.
2. **Text Processing**: Using **Langchain** and OpenAI's LLM, the combined text is split into smaller chunks, embeddings are generated, and stored in a vector search index using **FAISS**.
3. **Question Answering**: When a user inputs a question, the system retrieves the most relevant document chunks using FAISS and generates a response using the LLM.
4. **Web Interface**: A simple chat-like interface built using **Flask** and **JavaScript** allows users to interact with the system and ask questions.

## Features

- Supports multiple document formats: PDF and DOCX.
- Efficient text chunking and embedding with **Langchain**.
- Semantic search powered by **FAISS** for document retrieval.
- Real-time interaction with a question-answering system via a web interface.

## File Structure

- **filereading.py**: Handles reading PDF and DOCX files and combines the text from them.
- **textprocessing.py**: Splits the text, generates embeddings, and performs semantic search and question answering using Langchain and FAISS.
- **flaskapp.py**: The main Flask app that handles the web interface and routes user questions to the back-end processing.
- **script.js**: JavaScript file for handling the front-end chat functionality and making API requests to the Flask back-end.

## Setup Instructions

### Prerequisites

- Python 3.x
- OpenAI API Key (for generating text embeddings and using the LLM)
- Required Python libraries:
  - `Flask`
  - `python-docx`
  - `PyPDF2`
  - `langchain`
  - `openai`
  - `faiss-cpu`
  - `dotenv`

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RAG-Project
2. Install the required dependencies:

  - pip install -r requirements.txt

3. Set up your OpenAI API key in a .env file:

  - OPENAI_API_KEY=your-openai-api-key

4. Place your document files (PDFs and DOCXs) in the designated directory and update the file_paths variable in flaskapp.py to point to your documents.

### Running the Application
- To start the Flask server:

- python flaskapp.py
- Open your browser and go to http://127.0.0.1:5000/ to interact with the system via the web interface.

### Usage
- Change the address of PDF and DOCX documents in the flask_app.py file and run the file.
- Ask questions related to the document content through the web interface.
- The system will retrieve the most relevant parts of the document and generate an answer.
