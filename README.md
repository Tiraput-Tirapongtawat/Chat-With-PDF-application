# Chat-With-PDF-application
Chat with PDF using RAG, FastAPI, and LangChain This project demonstrates an intelligent document-querying system built with Python, FastAPI, and LLM libraries like LangChain and LlamaIndex, leveraging Retrieval-Augmented Generation (RAG) to enable natural language interactions with PDF files.

# Background
We are trying to catch up with the current trends in LLM, we have a bunch of papers
downloaded from the internet. We need your help to create a Chat With PDF application.

# Table of content
  1. How Does It Work?
  2. Running Locally with Docker Compose
  3. Future Improvements


# How Does It Work?
The API has three main endpoints:

Query Endpoint (/query/):

  Description: This endpoint accepts a user query and retrieves relevant context from a Chroma database.
  Process:
  The query is embedded using a language model.
  A similarity search is performed in Chroma to retrieve context based on the query.
  A prompt is dynamically generated, incorporating both the retrieved context and any prior conversation history.
  The generated prompt is sent to the language model, which produces a response.
  The query-response pair is stored in memory for future context.

Show History Endpoint (/history/):

  Description: Returns a history of all queries and responses in the current session.
  Usage: Useful for tracking conversation flow and providing a cohesive interaction experience for users.

Clear Memory Endpoint (/clear_memory/):

  Description: Resets the conversation memory, clearing any stored queries and responses.
  Usage: Allows users to start a new session without any retained context from previous interactions.


# Running Locally with Docker Compose

# Future Improvement


