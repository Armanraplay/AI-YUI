# self_modder.py

import os
from storage import Memory

MODIFIABLE_FILES = ["tools.py", "learner.py"]

def maybe_self_modify():
    log = Memory().load_log()
    if "ubah dirimu" in log or "modifikasi" in log:
        for file in MODIFIABLE_FILES:
            try:
                with open(file, "r+", encoding="utf-8") as f:
                    code = f.read()
                    # Contoh dummy: tambahkan komentar jika tidak ada
                    if "# Yui modified" not in code:
                        f.seek(0)
                        f.write("# Yui modified\n" + code)
                print(f"[Self-Mod] {file} dimodifikasi.")
            except Exception as e:
                print(f"[Self-Mod Error] {file}: {e}")

