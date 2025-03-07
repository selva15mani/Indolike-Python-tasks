import random

jokes = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why was the computer cold? It forgot to close Windows.",
    "Why did Python break up with Java? Too many class issues!"
]

def tell_joke():
    print("\nHere's a joke for you:")
    print(random.choice(jokes))

def main():
    while True:
        input("\nPress Enter to hear a joke...")
        tell_joke()
        if input("Want another one? (y/n): ") != 'y':
            print("Bye! Stay happy.")
            break

main()