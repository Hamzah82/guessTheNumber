import random

def guess_the_number():
    print("\n🎯 WELCOME TO THE GUESS THE NUMBER GAME! 🎯\n")

    while True:
        try:
            attempts = int(input("🔢 How many attempts do you want? "))
            number_range = int(input("📏 What is the maximum number to guess? "))

            if attempts <= 0 or number_range <= 0:
                print("⚠️ Please enter positive numbers!")
                continue
            break
        except ValueError:
            print("⚠️ Please enter a valid number!")

    secret_number = random.randint(1, number_range)
    previous_guess = None

    print("\n🎮 Game started! Try to guess the number.\n")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"⚡ Your guess ({attempts - attempt + 1} attempts left): "))
                if guess < 1 or guess > number_range:
                    print(f"⚠️ Enter a number between 1 and {number_range}!")
                    continue
                break
            except ValueError:
                print("⚠️ Enter a valid number!")

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempt} attempts! 🎉")
            break
        else:
            hint = "too high ⬆️" if guess > secret_number else "too low ⬇️"
            print(f"❌ Wrong! Your guess is {hint}. Try again!")

            if previous_guess is not None:
                if abs(secret_number - guess) < abs(secret_number - previous_guess):
                    print("🔥 You're getting closer!")
                else:
                    print("❄️ You're moving away!")

            previous_guess = guess
    else:
        print(f"\n😢 Oh no! You're out of attempts. The correct number was {secret_number}.")

    print("\n👋 Thanks for playing! See you next time!")

    play_again = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ["yes", "y"]:
        guess_the_number()
    else:
        print("\n🎮 Game Over! Have a great day! 🎉")

guess_the_number()
