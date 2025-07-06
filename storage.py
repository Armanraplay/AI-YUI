# storage.py

import json
from config import PROMPT_LOG_PATH

class Memory:
    def __init__(self):
        self.log_path = PROMPT_LOG_PATH

    def save_interaction(self, user_input):
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"User: {user_input}\n")

    def load_log(self):
        try:
            with open(self.log_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return ""
