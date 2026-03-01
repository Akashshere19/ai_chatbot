class Memory:

    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append(f"{role}: {message}")

    def get(self, k=5):
        return "\n".join(self.history[-k:])
    
memory = Memory()    