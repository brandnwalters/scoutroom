import anthropic
import sys
from data import load_players, format_players_for_prompt

def run_scout(brief: str, players: list[dict]) -> str:
    """Sends a brief and list of players to Claude with a system prompt,
    returns the model's text response"""
    client = anthropic.Anthropic()

    print(f"calling API, prompt length: {len(brief)}")
    message = client.messages.create(
        model= 'claude-haiku-4-5',
        max_tokens= 1500,
        system="""You are the head scout of a prestigious european footballing institution. When given a brief 
        and list of players, you look at the different statistics for each player and return the top 5 names, ranked, 
        that fit what the user is looking for. You may only look at stats from the table provided and must give a 
        line of reasoning for each player you reccommend, citing specific numbers.""",
        messages=[{"role": "user", "content": f"{brief}, {format_players_for_prompt(players)}"}]
    )
    return message.content[0].text

if __name__ == "__main__":
    print("starting")
    brief = sys.argv[1]
    print(f"brief: {brief}")
    players = load_players()
    print(f"loaded {len(players)} players")
    result = run_scout(brief, players)
    print("scout returned")
    print(result)