# tools.py

from config import GROK_API_KEY, GEMINI_API_KEY, API_PROVIDER_PRIORITY
import google.generativeai as genai
import datetime

# Konfigurasi Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def run_local_llm(prompt: str) -> str:
    # Placeholder simulasi lokal
    return f"[Offline] {prompt.capitalize()} (simulasi)"

def fallback_to_api(prompt: str) -> str:
    for provider in API_PROVIDER_PRIORITY:
        if provider == "GROK":
            try:
                return call_grok_api(prompt)
            except Exception as e:
                print(f"[Grok Fallback Error] {e}")
        elif provider == "GEMINI":
            try:
                # Menggunakan model Gemini 2.5 Flash
                model = genai.GenerativeModel("models/gemini-2.5-flash")
                response = model.generate_content(prompt)
                return response.text.strip()
            except Exception as e:
                print(f"[Gemini Fallback Error] {e}")
    return "[API Error] Semua provider gagal."

def call_grok_api(prompt: str) -> str:
    # Simulasi Grok: ubah jika kamu punya endpoint API
    if GROK_API_KEY == "your-grok-api-key":
        raise ValueError("API Key Grok belum diatur.")
    return f"[Grok API] Jawaban untuk: {prompt}"
