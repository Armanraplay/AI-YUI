# nlp.py

import re

def process_input(text: str) -> str:
    # Bersihkan dan normalisasi input
    text = text.lower().strip()
    text = re.sub(r'[^\w\s,.!?]', '', text)
    return text
