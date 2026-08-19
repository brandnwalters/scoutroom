import os
import sys
import json
from utils import parse_json_response
from agents import DATA_ANALYST, NEWS_RESEARCHER, SPORTING_DIRECTOR, HEAD_SCOUT, RECRUITMENT_DIRECTOR
from data import format_players_for_prompt, load_players

def build_dossier(player: dict, scout_pick: dict) -> dict:
    pid = player["player_id"]
    analyst_input = f"""Player: {player['name']} | Age: {player['age']} | Position: {player['position']} | 
    Club: {player['club']} | League: ({player['league']}) | 
    Minutes: {player['minutes']} | Goals: {player['goals']} | xG: {player['xg']} |
    Assists: {player['assists']} | xA: {player['xa']} | Progressive Carries: {player['progressive_carries']} | 
    Tackles won: {player['tackles_won']} | Pass Completion Pct: {player['pass_completion_pct']}
    """
    path = f"data/news/{pid}.txt"
    if os.path.exists(path):
        news_text = open(path).read()
    else:
        news_text = "No news articles found for this player."

    news_input = f"Player: {player['name']}\n\nARTICLES:\n{news_text}"

    finance_input= f"""Player: {player['name']} | Market Value: {player['market_value_m']} | Contract Expiry {player['contract_expires']}"""

    return {
        "player_id": pid,
        "player_row": player,
        "scout": scout_pick,
        "analyst": parse_json_response(DATA_ANALYST.run(analyst_input)),
        "news": parse_json_response(NEWS_RESEARCHER.run(news_input)),
        "finance": parse_json_response(SPORTING_DIRECTOR.run(finance_input)),
    }


def run_recruitment(brief: str, players:list[dict]) -> dict:
    scout_picks = parse_json_response(HEAD_SCOUT.run(f"{brief}, {format_players_for_prompt(players)}"))
    players_by_id = {p["player_id"]: p for p in players}
    shortlist = []
    for pick in scout_picks:
        pid = pick["player_id"]
        if pid in players_by_id:
            shortlist.append((players_by_id[pid], pick))
        else:
            print(f"⚠️  Scout returned unknown player_id: {pid} — dropping")

    dossiers = [build_dossier(row, scout_pick) for row, scout_pick in shortlist]
    print(json.dumps(dossiers[0], indent=2))
    decision = parse_json_response(RECRUITMENT_DIRECTOR.run(json.dumps(dossiers), max_tokens=4000))
    return {"decision": decision, "dossiers": dossiers}

if __name__ == "__main__":
    players = load_players()
    result = run_recruitment(sys.argv[1], players)
    print(json.dumps(result["decision"], indent=2))

