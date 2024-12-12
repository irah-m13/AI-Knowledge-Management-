class BaseAIModel:
    def generate_response(self, prompt: str):
        raise NotImplementedError("Subclasses must implement this method")
