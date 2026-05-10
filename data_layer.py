import json
from pathlib import Path


def load_data(file_path):
    """Load JSON data from a file. Returns empty list if file doesn't exist."""
    path = Path(file_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(file_path, data):
    """Save data as JSON to a file."""
    path = Path(file_path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
