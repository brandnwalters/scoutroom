import anthropic
from prompts import HEAD_SCOUT_PROMPT, DATA_ANALYST_PROMPT, NEWS_RESEARCHER_PROMPT, SPORTING_DIRECTOR_PROMPT, RECRUITMENT_DIRECTOR_PROMPT
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

HEAD_SCOUT = Agent(name="Head Scout", emoji="⚽", system_prompt=HEAD_SCOUT_PROMPT)
DATA_ANALYST = Agent(name="Data Analyst", emoji="📊", system_prompt=DATA_ANALYST_PROMPT)
NEWS_RESEARCHER = Agent(name="News Researcher", emoji="📰", system_prompt=NEWS_RESEARCHER_PROMPT)
SPORTING_DIRECTOR = Agent(name="Sporting Director", emoji="💰", system_prompt=SPORTING_DIRECTOR_PROMPT)
RECRUITMENT_DIRECTOR= Agent(name="Recruitment Director", emoji="🎯", system_prompt= RECRUITMENT_DIRECTOR_PROMPT, model="claude-sonnet-5")