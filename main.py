from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from embedding import get_embedding_function
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os

app = FastAPI()

CHROMA_PATH = "chroma"
os.environ["OPENAI_API_KEY"] = 'your api key'

PROMPT_TEMPLATE = """
Answer the question based only on the following context and prior conversation history:

{context}

---

Conversation history:
{history}

---

Answer the question based on the above context and conversation history: {question}
"""

# Initialize the conversation memory globally to keep it persistent across requests
memory = ConversationBufferMemory(return_messages=True)

# Initialize the embedding and Chroma DB only once for efficiency
embedding_function = get_embedding_function()
db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

class QueryRequest(BaseModel):
    query_text: str

@app.get("/")
async def root():
    return {"message": "Welcome to RAG"}

@app.post("/query/")
async def query_rag(request: QueryRequest):
    query_text = request.query_text

    # Search the DB
    results = db.similarity_search_with_score(query_text, k=3)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # Prepare the prompt
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(
        context=context_text,
        question=query_text,
        history=memory.buffer  # Pass conversation history
    )

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    # Add response to memory
    memory.save_context({"query": query_text}, {"response": response_text})

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = {
        "response": response_text,
        "sources": sources
    }
    return formatted_response

@app.get("/history/")
async def show_history():
    """Endpoint to show the conversation history."""
    history = []
    
    # Iterate over messages in memory buffer
    for message in memory.buffer:
        if message.type == "human":
            # HumanMessage objects represent user queries
            history.append({"query": message.content, "response": None})
        elif message.type == "ai":
            # AIMessage objects represent responses from the AI
            if history and history[-1]["response"] is None:
                # Update the last query's response
                history[-1]["response"] = message.content
            else:
                # In case there's an AI message without a query
                history.append({"query": None, "response": message.content})
                
    return {"history": history}

@app.post("/clear_memory/")
async def clear_memory():
    """Endpoint to clear the conversation memory."""
    global memory
    memory = ConversationBufferMemory(return_messages=True)
    return {"message": "Memory cleared"}

