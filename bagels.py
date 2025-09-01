import random

NUM_OF_GUESSES = 10
NUM_OF_DIGITS = 3


def generate_random_number(digits=NUM_OF_DIGITS):
    if digits == 1:
        return str(random.randint(0, 9))
    else:
        lower = 10**(digits-1)     # np. dla 3 → 100
        upper = 10**digits - 1     # np. dla 3 → 999
        return str(random.randint(lower, upper))


def compare_number(number, guess):
    if number != guess:
        clues = []
        for i in range(len(guess)):
            if guess[i] not in number:
                continue
            elif guess[i] == number[i]:
                clues.append("Fermi")
            else:
                clues.append("Pico")

        if not clues:
            print("Bagels")
        else:
            print(" ".join(clues))
        return False
    else:
        print("You got it!")
        return True


def intro():
    print(f"Bagels - A Deductive Logic Game\n"
          f"By Dawid Michalec\n\n"
          f"I am thinking of a 3-digit number. Try to guess what it is.\n"
          f"Here are some clues:\n\n"
          f"When I say:    That means:\n"
          f"Pico    One digit is correct but in the wrong position.\n"
          f"Fermi    One digit is correct and in the right position.\n"
          f"Bagels    No digit is correct.\n\n"
          f"I have thought up a number.\n"
          f"You have {NUM_OF_GUESSES} guesses to get it.\n")


def play_game():
    number = generate_random_number()
    print(f"(DEBUG: {number})")
    for attempt in range(1, NUM_OF_GUESSES + 1):
        while True:
            guess = input(f"Guess #{attempt}:\n")
            if len(guess) == NUM_OF_DIGITS and guess.isdigit():
                break
            print(f"Number must contain {NUM_OF_DIGITS} digits!")

        if compare_number(number, guess):
            return True
    return False


def ask_yes_no(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ("yes", "no"):
            return choice == "yes"
        print("You need to type yes or no!")


def main():
    while True:
        intro()
        win = play_game()
        if win:
            again = ask_yes_no("You got it! Do you want to play again? (yes/no): ")
        else:
            again = ask_yes_no("You lost. Do you want to play again? (yes/no): ")
        if not again:
            print("Have a nice day!")
            break


main()
