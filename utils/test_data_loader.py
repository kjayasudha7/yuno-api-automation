python
import json
from pathlib import Path

def load_customers():
    file_path = Path(__file__).parent.parent / "test_data" / "customers.json"
    with open(file_path) as file:
        return json.load(file)

def load_cards():
    file_path = Path(__file__).parent.parent / "test_data" / "cards.json"
    with open(file_path) as file:
        return json.load(file)
