import anthropic

client = anthropic.Anthropic()

class Agent:
    def __init__(self, name, emoji, system_prompt, model='claude-haiku-4-5'):
        self.name = name
        self.emoji = emoji
        self.system_prompt = system_prompt
        self.model = 'claude-haiku-4-5'
    
    def run(self, user_message: str, max_tokens:int = 1500) -> str:
        response = client.messages.create(
            model= self.model,
            max_tokens= 1500,
            system=self.system_prompt,
            messages=[{"role":"user", "content": user_message}]
        )
        return response.content[0]
