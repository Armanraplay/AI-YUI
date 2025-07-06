# config.py

YUI_NAME = "Yui"
YUI_VERSION = "0.1"
YUI_MODE = "HYBRID"  # Options: LOCAL, API, HYBRID

# Model lokal
LLM_MODEL_PATH = "models/mistral-7b.Q4_K_M.gguf"

# API fallback
USE_API = True
API_PROVIDER_PRIORITY = ["GEMINI", "GROK"]  # Urutan fallback
GROK_API_KEY = "your-grok-api-key"
GEMINI_API_KEY = "AIzaSyC59lmHBoupXPk0HxXtgvsYYNvefpxLoVI"

# Fitur self-learn dan self-edit
ALLOW_SELF_MOD = True
PROMPT_LOG_PATH = "prompt_log.txt"
