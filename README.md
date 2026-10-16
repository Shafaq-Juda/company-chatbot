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

```text
company-chatbot/
├── app.py
├── policies.txt
├── requirements.txt
└── README.md
