from fastapi import APIRouter
from app.agents.router_agent import RouterAgent

router = APIRouter()
agent = RouterAgent()

# @router.post("/chat")
# def chat(message: str):
#     return {"response": agent.route(message)}




@router.get("/chat")
def chat(prompt: str):

    print("API RECEIVED:", prompt)

    response = agent.route(prompt)

    return {"response": response}