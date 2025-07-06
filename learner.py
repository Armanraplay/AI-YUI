# learner.py

from storage import Memory

def learn_from_log():
    log = Memory().load_log()
    keywords = set()
    for line in log.splitlines():
        if "User:" in line:
            words = line.replace("User:", "").strip().split()
            for word in words:
                if len(word) > 4:
                    keywords.add(word.lower())
    return f"Aku belajar kata-kata penting: {', '.join(sorted(keywords))}"

