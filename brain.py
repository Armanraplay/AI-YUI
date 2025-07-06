# brain.py

from config import YUI_MODE, USE_API, ALLOW_SELF_MOD
from nlp import process_input
from storage import Memory
from tools import fallback_to_api, run_local_llm
from learner import learn_from_log
from self_modder import maybe_self_modify
from game_chess_gui import play_chess_gui  # ✅ Tambahan

class YuiBrain:
    def __init__(self):
        self.memory = Memory()
        if ALLOW_SELF_MOD:
            maybe_self_modify()

    def respond(self, text: str) -> str:
        processed = process_input(text)
        self.memory.save_interaction(text)
        response = ""

        # ✅ Trigger jika ingin bermain catur
        if "main catur" in text.lower():
            play_chess_gui()
            return "Selesai bermain catur!"

        if YUI_MODE == "LOCAL":
            response = run_local_llm(processed)

        elif YUI_MODE == "API" and USE_API:
            response = fallback_to_api(processed)

        elif YUI_MODE == "HYBRID":
            try:
                response = run_local_llm(processed)
                if "[Offline]" in response:
                    raise ValueError("Model lokal dummy.")
            except Exception:
                response = fallback_to_api(processed)

        return response
