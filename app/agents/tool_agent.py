import asyncio
import json
from app.agents.base_agent import BaseAgent
from app.mcp.client import MCPToolClient
from app.llm.ollama_client import llm


# class ToolAgent(BaseAgent):

#     def run(self, query):

#         async def execute():

#             client = MCPToolClient()
#             # await client.connect()
#             city = query.split('in')
#             print('city:::',city)

#             if "weather" in query.lower():
#                 return await client.call_tool(
#                     "weather",
#                     {"city": "Pune"}
#                 )

#             if "files" in query.lower():
#                 return await client.call_tool(
#                     "list_files",
#                     {}
#                 )

#         return asyncio.run(execute())


# import asyncio
# import json
# from app.agents.base_agent import BaseAgent
# from app.mcp.client import MCPToolClient
# from app.llm.ollama_client import llm


class ToolAgent(BaseAgent):

    def run(self, query: str):

        async def execute():

            client = MCPToolClient()

            # 🧠 Ask LLM which tool + arguments
            prompt = f"""
Extract tool usage from user request.

Available tool:
weather(city)

Return ONLY JSON:

{{
  "tool": "weather",
  "arguments": {{
      "city": "<city>"
  }}
}}

User request:
{query}
"""

            decision = llm.generate(prompt).strip()

            print("TOOL JSON:", decision)

            tool_call = json.loads(decision)

            result = await client.call_tool(
                tool_call["tool"],
                tool_call["arguments"]
            )

            return result

        return asyncio.run(execute())