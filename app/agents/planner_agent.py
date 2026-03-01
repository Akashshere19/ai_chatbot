from app.agents.base_agent import BaseAgent
from app.llm.ollama_client import  llm

class PlannerAgent(BaseAgent):

    def run(self, goal):

        prompt  = f"""
Create MAXIMUM 3 short execution steps.

Goal:
{goal}

Return concise numbered steps only.
"""

        plan = llm.generate(prompt)

        return plan