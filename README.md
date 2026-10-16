# AI Company Policy Chatbot

A local AI chatbot built with Python, LangChain, Ollama, and Retrieval-Augmented Generation (RAG).

## Project Overview

This project demonstrates how an AI assistant can retrieve relevant information from company policy documents and answer user questions using a locally running language model.

The chatbot also demonstrates how to handle questions when the available policy documents do not contain the requested information.

## Features

- Answers questions about shipping, returns, and customer support.
- Loads policies from an external text file.
- Splits documents into smaller chunks.
- Uses embeddings and cosine similarity to retrieve relevant information.
- Generates answers using a local LLM.
- Tests behavior for both available and missing information.

## Technologies

- Python
- LangChain
- Ollama
- Qwen 2.5 3B
- Nomic Embed Text
- Retrieval-Augmented Generation (RAG)

## Project Structure

company-chatbot/
├── app.py
├── policies.txt
├── requirements.txt
└── README.md

## Setup

1. Install Python and Ollama
Install Python and download Ollama from:

https://ollama.com/ 

2. Download the models
Run these commands in your terminal:


ollama pull qwen2.5:3b
ollama pull nomic-embed-text

3. Create and activate a virtual environment
On Windows:

python -m venv .venv
.venv\Scripts\activate.bat

4. Install dependencies

python -m pip install -r requirements.txt

5. Run the chatbot

python app.py

Type exit to close the chatbot.

## Sample Test Results

## Question and Their Expected result

- How long does shipping take?

3 to 5 business days

- When should I report a damaged product?

Within 48 hours

- What are the company's vacation benefits?

The chatbot says it does not know

## How RAG Works

- Load company policies from policies.txt.

- Split the text into smaller chunks.

- Convert policy chunks into embeddings.

- Convert the user's question into an embedding.

- Retrieve the most similar policy chunk using cosine similarity.

- Pass the retrieved text to the language model to generate an answer.

## Limitations
- Uses a small sample policy document.

- Uses a basic similarity threshold that requires further evaluation.

- The language model may occasionally generate incorrect answers.

- Requires Ollama and local models to be installed.

- Runs in the terminal; it does not currently have a web interface.

## Future Improvements

- Add more policy documents.

- Improve retrieval evaluation and automated testing.

- Build a browser-based interface.

- Explore deployment options.

## Learning Goals

This project was built to develop practical skills in Python, LLM integration, LangChain, embeddings, semantic search, and RAG.
