import random

messages = {
    "low": [
        "Stay strong, better days are coming 🌤️",
        "Even the darkest night will end and the sun will rise.",
    ],
    "mid": [
        "Keep going, you're doing fine!",
        "Today is a good day to try something new.",
    ],
    "high": [
        "You're shining! Keep up the great mood 🌟",
        "Your positivity is contagious!",
    ],
}

def get_mood_message(score):
    if score < 4:
        return random.choice(messages["low"])
    elif score < 7:
        return random.choice(messages["mid"])
    else:
        return random.choice(messages["high"])

def main():
    try:
        score = int(input("Rate your mood (1-10): "))
        if 1 <= score <= 10:
            print(get_mood_message(score))
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("That must be a number!")

if __name__ == "__main__":
    main()
