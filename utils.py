import json

def extract_json_span(text: str) -> str:
    starts = []
    for i in (text.find("["), text.find("{")):
        if i != -1:
            starts.append(i)
    if not starts:
        raise Exception(f"No brackets found at beggining: {text[:300]}")
    start = min(starts)

    ends=[]
    for i in (text.find("]"), text.find("}")):
        if i != -1:
            ends.append(i)
    if not ends:
        raise Exception(f"No brackets found at end: {text[:300]}")
    end = max(ends) + 1

    return text[start:end]



def parse_json_response(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    cleaned = extract_json_span(text.strip())

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise Exception(
            f"Could not parse JSON after cleaning\n"
            f"Raw response: {text[:300]}"
        ) from e
    

