import json
from pathlib import Path


INVENTORY_PATH = Path("inventory.json")
SALES_PATH = Path("sales.json")
USERS_PATH = Path("users.json")


def load_data(filepath):
    path = Path(filepath)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(filepath, data):
    path = Path(filepath)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_users():
    data = load_data(USERS_PATH)
    return data

