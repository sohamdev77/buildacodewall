import random

def evaluate_code(code: str) -> int:
    """Very basic logic to evaluate code strength"""
    strength = 0
    keywords = ["if", "for", "while", "def", "class", "public", "return", "import", "print"]
    for word in keywords:
        if word in code:
            strength += 10
    strength += len(code) // 10  # longer code slightly stronger
    return min(strength, 100)  # cap at 100


def show_wall(strength: int):
    if strength >= 50:
        print("\n🧱 Your Code is STRONG! A Wall has been built! 🧱\n")
        print("▓" * (strength // 2))
    else:
        print("\n🔨 Weak Code! The Hammer Strikes! 🔨\n")


def game():
    print("=== Welcome to BUILD A CODE WALL ===")
    print("Languages available: Python, Java, C++, C, JavaScript")
    lang = input("Choose your language: ").strip().lower()
    if lang not in ["python", "java", "c++", "c", "javascript"]:
        print("Invalid choice. Exiting.")
        return

    print("\nChoose difficulty level: Easy / Medium / Hard")
    level = input("Level: ").strip().lower()
    print(f"\nYou selected {lang.title()} at {level.title()} level!")

    print("\nNow, type your code (single line or multiple lines).")
    print("Enter 'END' in a new line when you’re done.\n")

    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line)

    code = "\n".join(code_lines)
    strength = evaluate_code(code)
    show_wall(strength)

    score = strength + random.randint(1, 20)
    print(f"🎯 Your Score: {score}/120\n")


if __name__ == "__main__":
    game()
