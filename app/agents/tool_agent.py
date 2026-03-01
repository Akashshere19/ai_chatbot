from app.rag.rag import search
from app.tools.filesystem import list_files

class ToolAgent:
    def run(self, query: str):
       
        if "list files" in query.lower():
            return str(list_files())

        # 1️⃣ Retrieve context
        context = search(query)


        if not context:
            return "I could not find relevant information."