# interface.py

def run_interface(brain):
    print("Yui: Halo, aku Yui. Ada yang bisa kubantu hari ini?")
    while True:
        try:
            user_input = input("Kamu: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Yui: Sampai jumpa!")
                break
            response = brain.respond(user_input)
            print(f"Yui: {response}")
        except KeyboardInterrupt:
            print("\nYui: Sampai jumpa!")
            break
