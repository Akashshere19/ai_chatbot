import requests


class OllamaClient:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "qwen2.5:7b"

    def generate(self, prompt: str):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 512,
                    "num_ctx": 2048
                }
            },
            timeout=600
        )
        print("RAW RESPONSE:", response.text)
        response.raise_for_status()
        data = response.json()
        text = data.get("response")
        if not text:
            return "I am here. How can assists you?"
        return text 

        # return response.json()["response"]


llm = OllamaClient()