from app.agents.base_agent import BaseAgent
from app.llm.ollama_client import llm
from app.memory.memory import memory


class ChatAgent(BaseAgent):

    def run(self, query: str):

        print("CHAT AGENT RUNNING")
        memory.add("user",query)

        prompt = f"""
                Conversation:
                {memory.get()}

                Assistant:
                """

        response = llm.generate(prompt)
        memory.add("assistant",response)

        print("CHAT RESPONSE:", response)

        return response or "Hello! How can I help you?"