import json
import os

def load_memory(session_id):
    path = f"{session_id}.json"
    if os.path.exists(path):
        return json.load(open(path))
    return []

def save_memory(session_id, memory):
    with open(f"{session_id}.json", "w") as f:
        json.dump(memory, f, indent=2)
