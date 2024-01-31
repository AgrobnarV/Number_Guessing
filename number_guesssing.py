import random


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Attention! Add only integer digit")


def play_guessing_game(lower_limit, upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print(f"Guess a number from {lower_limit} to {upper_limit}")

    while True:
        guess = get_integer_input(f"Guess the number: ")

        attempts += 1

        if guess < secret_number:
            print(f"Attempt {attempts}: Too low, try again")
        elif guess > secret_number:
            print(f"Attempt {attempts}: Too high, try again")
        else:
            print(f"Attempt {attempts}: You guessed it, my congrats! The secret number was {secret_number}")
            break


def play_fingers_game(lower_limit, upper_limit):
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    fingers = 5

    print(f"Guess a number from {lower_limit} to {upper_limit}. You have {fingers} fingers")

    while fingers > 0:
        guess = get_integer_input(f"Guess the number: ")

        attempts += 1

        if guess == secret_number:
            print(
                f"Attempt {attempts}: You guessed it, my congrats! The secret number was {secret_number} "
                f"You have {fingers} fingers left.")
            break
        else:
            print(f"Attempt {attempts}: Wrong! You lose a finger. You have {fingers - 1} fingers left")
            fingers -= 1

    if fingers == 0:
        print("You have no more fingers. Game over :( ")


def main():
    play_again = True

    while play_again:
        lower_limit = get_integer_input("Enter the lower limit (integer): ")
        upper_limit = get_integer_input("Enter the upper limit (integer): ")

        while upper_limit <= lower_limit:
            print("Error! The upper limit must be greater than the lower one.")
            upper_limit = get_integer_input("Enter the upper limit (integer): ")

        game_mode = input("Choose a game mode: 'guessing game' or 'fingers': ").lower()

        if game_mode == 'guessing' or game_mode == 'guessing game':
            play_guessing_game(lower_limit, upper_limit)
        elif game_mode == 'fingers' or game_mode == 'finger':
            play_fingers_game(lower_limit, upper_limit)
        else:
            print("Error! Invalid game mode. Choose 'guessing game' or 'fingers'")

        play_again = input("Do you wanna play again? (yes/no): ").lower() == 'yes'

    print("Thank you for playing. See you again...")


if __name__ == "__main__":
    main()
