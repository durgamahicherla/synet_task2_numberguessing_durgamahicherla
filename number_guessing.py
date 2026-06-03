import random

def number_guessing_game():
    print("=" * 40)
    print("   🎮 Welcome to Number Guessing Game!")
    print("=" * 40)

    # Random number generate cheyyi (1 to 100)
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"\n🔢 I'm thinking of a number between 1 and 100.")
    print(f"🎯 You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        # User input teesuko
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} → Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue

        attempts += 1

        # Check the guess
        if guess < secret_number:
            remaining = max_attempts - attempts
            print(f"📈 Too Low! Try a higher number. ({remaining} attempts left)\n")

        elif guess > secret_number:
            remaining = max_attempts - attempts
            print(f"📉 Too High! Try a lower number. ({remaining} attempts left)\n")

        else:
            print("=" * 40)
            print(f"🎉 Correct! You guessed it!")
            print(f"✅ The number was: {secret_number}")
            print(f"🏆 You did it in {attempts} attempt(s)!")
            print("=" * 40)

            # Score based on attempts
            if attempts <= 3:
                print("🌟 Amazing! You're a genius!")
            elif attempts <= 6:
                print("👍 Great job!")
            else:
                print("😅 You made it, but try to do better next time!")
            return

    # Attempts exhausted
    print("=" * 40)
    print(f"😢 Game Over! You've used all {max_attempts} attempts.")
    print(f"🔍 The secret number was: {secret_number}")
    print("=" * 40)

def main():
    while True:
        number_guessing_game()
        print()
        play_again = input("🔄 Play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    main()
