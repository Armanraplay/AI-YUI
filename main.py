# main.py

from config import YUI_NAME, YUI_MODE
from interface import run_interface
from brain import YuiBrain

def main():
    print(f"{YUI_NAME} is starting in {YUI_MODE} mode...")
    brain = YuiBrain()
    run_interface(brain)

if __name__ == "__main__":
    main()
