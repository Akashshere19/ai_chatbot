from app.agents.base_agent import BaseAgent
from app.rag.rag import search
from app.llm.ollama_client import llm


from app.agents.base_agent import BaseAgent
from app.rag.rag import search
from app.llm.ollama_client import llm


class RAGAgent(BaseAgent):

    def run(self, query: str):

        docs = search(query)
        print('docs:::',docs)

        if not docs:
            return "No information found."

        context = "\n\n".join(docs)

        prompt = f"""
                    Answer using ONLY the context below.

                    Context:
                    {context}

                    Question:
                    {query}

                    Answer:
                """
        print("FINAL CONTEXT:\n", context)
        response = llm.generate(prompt)
        print('final response:::',response)

        return response
    

    