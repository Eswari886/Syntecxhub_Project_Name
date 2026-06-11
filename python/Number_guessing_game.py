import random

def play_game():
    print("\n=== Number Guessing Game ===")

    print("Select Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        limit = 50
    elif choice == "2":
        limit = 100
    elif choice == "3":
        limit = 200
    else:
        print("Invalid choice! Setting Medium level.")
        limit = 100

    secret_number = random.randint(1, limit)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {limit}: "))
            attempts += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")

best_score = None

while True:
    score = play_game()

    if best_score is None or score < best_score:
        best_score = score

    print("Best Score:", best_score)

    replay = input("Do you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("Thank you for playing!")
        break