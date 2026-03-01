from app.agents.chat_agent import ChatAgent
from app.agents.rag_agent import RAGAgent
from app.agents.tool_agent import ToolAgent
from app.agents.planner_agent import PlannerAgent
from app.llm.ollama_client import llm


class RouterAgent:

    def route(self, query: str):

        print("query:::", query)

        routing_prompt = f"""
You are a router.

Choose which agent should handle the query.

Agents:
chat   -> general conversation
rag    -> document knowledge
tool   -> actions
plan   -> multi-step goals
memory -> questions about previous conversation

Return ONLY:
chat | rag | tool | plan | memory

Query: {query}
"""

        decision = llm.generate(routing_prompt).strip().lower()

        print("ROUTER DECISION:", decision)

        if decision == "plan":
            print("→ PLANNER AGENT")
            return PlannerAgent().run(query)

        elif decision == "tool":
            print("→ TOOL AGENT")
            return ToolAgent().run(query)

        elif decision == "rag":
            print("→ RAG AGENT")
            return RAGAgent().run(query)
        
        elif decision == "memory":
            print("-> MEMORY called")
            return ChatAgent().run(query)

        else:
            print("→ CHAT AGENT")
            return ChatAgent().run(query)