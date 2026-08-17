import pandas as pd

def load_players(path="data/players.csv") -> list[dict]:
    """reads the csv and turns all the columns to numbers before returning dataFrame"""
    df = pd.read_csv(path)
    return df.to_dict("records")

def format_players_for_prompt(players: list[dict]) -> str:
    """Turns the player list into text table for the model to read with one player per line """
    lines = []
    lines.append("Headers: player_id | name | age | position | minutes |"
    "xg | progressive_carries | tackles_won | pass_completion_pct\n")
    for p in players:
        lines.append(f"""{p['player_id']} | {p['name']} | {p['age']} | {p['position']} | {p['minutes']} |
                     {p['xg']} | {p['progressive_carries']} | {p['tackles_won']} | {p['pass_completion_pct']}""")
    return "\n".join(lines)