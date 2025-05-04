from fastapi import FastAPI
from pydantic import BaseModel
from backend.agent import get_agent_response

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: Query):
    response = get_agent_response(query.message)
    return {"response": response}
