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


**Create data base**

1. Prepare the Database Folder: Create a folder for your database and place the PDF files you want to interact with in this folder.
2. Specify Path: In create_datadb.py, specify the path to the database folder.
3. Generate the Chroma Database: Run create_datadb.py to initialize the Chroma database. This will create a chroma folder to store the embeddings.

The API has three main endpoints:
**Query Endpoint (/query/):**

  Description: This endpoint accepts a user query and retrieves relevant context from a Chroma database.
  Process:
  The query is embedded using a language model.
  A similarity search is performed in Chroma to retrieve context based on the query.
  A prompt is dynamically generated, incorporating both the retrieved context and any prior conversation history.
  The generated prompt is sent to the language model, which produces a response.
  The query-response pair is stored in memory for future context.

**Show History Endpoint (/history/):**

  Description: Returns a history of all queries and responses in the current session.
  Usage: Useful for tracking conversation flow and providing a cohesive interaction experience for users.

**Clear Memory Endpoint (/clear_memory/):**

  Description: Resets the conversation memory, clearing any stored queries and responses.
  Usage: Allows users to start a new session without any retained context from previous interactions.

Example Commands
After running main.py, use the following commands to interact with the API:

1. Ask question :
   'curl -X POST "http://127.0.0.1:8000/query/" -H "Content-Type: application/json" -d "{\"query_text\": \"What is SQL?\"}"'
2. Clear history
   'curl -X POST "http://127.0.0.1:8000/clear_memory/" -H "Content-Type: application/json"'
3. Show history
   'curl -X GET "http://127.0.0.1:8000/history/"'
   
# Running Locally with Docker Compose
To build and run the application with Docker Compose, use the following command:
'docker-compose up -d --build'


# Future Improvement

**1.Enhanced Query Processing:**

Incorporate more sophisticated embeddings or custom-trained models to improve context retrieval.
Introduce mechanisms to better handle ambiguous queries by asking clarifying questions.

**2. Scalability and Performance:**
   
Implement caching for frequently accessed information to reduce response latency.
Consider using Redis or another in-memory database for faster retrieval of conversation history and embedding cache.

**3. Security Enhancements:**

Add authentication and authorization to restrict access to the API.
Encrypt sensitive data, such as API keys, using secure key management practices.

**4. Analytics and Monitoring:**

Integrate logging and monitoring solutions (e.g., Prometheus, Grafana) to track metrics like latency, error rates, and user interactions.
Use these insights to improve system performance and user experience.
User Feedback Mechanism:

**5. User Feedback Mechanism:**

Introduce a feedback system that allows users to rate responses. Use this data to improve model performance or adjust response generation.
Language Support:

**6. Language Support:**

Enable multi-language support to expand usability for a global audience.

