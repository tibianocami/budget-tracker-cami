import json
import os

def load_data(filepath: str) -> list:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("[Errore] Il file dei dati è corrotto. Caricata lista vuota.")
        return []

def save_data(filepath: str, data_list: list) -> bool:
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data_list, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"[Errore] Impossibile salvare i dati: {e}")
        return False
