from app.agents.chat_agent import ChatAgent
from app.agents.rag_agent import RAGAgent
from app.agents.tool_agent import ToolAgent
from app.agents.planner_agent import PlannerAgent
from app.llm.ollama_client import llm


class RouterAgent:

    def route(self, query: str):

        print("query:::", query)

        routing_prompt = f"""
                You are an intelligent router.

                Agents:

                chat:
                - general knowledge
                - definitions
                - explanations
                - normal conversation

                rag:
                - questions about stored documents
                - project knowledge
                - uploaded data
                - internal information

                tool:
                - real-world actions or APIs
                - requires LIVE or REAL-TIME data
                - weather
                - filesystem
                - APIs
                - external information

                plan:
                - multi-step goals



                memory:
                - questions about previous conversation

                IMPORTANT:
                Weather queries ALWAYS use tool.
                
                Return ONLY:
                chat | rag | tool | plan | memory

                Query:
                {query}
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
            if "document" not in query.lower()\
                and "project" not in query.lower()\
                and "my" not in query.lower():
                decision = "chat"
            return RAGAgent().run(query)
        
        elif decision == "memory":
            print("-> MEMORY called")
            return ChatAgent().run(query)

        else:
            print("→ CHAT AGENT")
            return ChatAgent().run(query)