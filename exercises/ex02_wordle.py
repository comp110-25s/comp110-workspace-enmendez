"""Wordle game that prompts user to guess a word that matches the length of the secret word"""

__author__ = "730751590"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_string: str, find_char: str) -> bool:
    """Checks if a single character is present in a given string"""
    assert len(find_char) == 1, f"len('{find_char}') is not 1"
    i: int = 0
    # Ensures the indices are less than the length of the search "word"
    # If the indices are greater than the length, the code will not execute
    # If the search "word" index is equal to a single character, it returns True
    # It increments to the next index position after it returns True until it becomes False
    while i < len(search_string):
        if search_string[i] == find_char:
            return True
        i += 1

    return False


def emojified(guess_string: str, secret_string: str) -> str:
    """Returns a color for the box based on the secret guess.
    It will have a white box for any letter of the secret not in the guess
    It will have a green box for a letter in the guess and secret that matches the same position
    It will have a yellow box for a letter in the guess that is in the secret but not the same position
    """
    assert len(guess_string) == len(
        secret_string
    ), "Guess must be same length as secret"
    i: int = 0
    # Executes an empty string for the hex code boxes to append to the list
    emoji_string: str = ""

    # Ensures the indices are less than the length of the guess "word"
    # If the guess index position aligns with the secret index position, it will result in GREEN
    # If the secret "word" is equal to any index position or single char of the guess "word", it will result in YELLOW
    # Otherwise, it will result in WHITE because there are no matched index positions with the secret "word"
    # It increments through every index position through a while loop
    # It appends the hex color box to the emoji string based on the condition
    # It returns the emoji string for the color hex codes to display in the program
    while i < len(guess_string):

        if guess_string[i] == secret_string[i]:
            emoji_string += GREEN_BOX
        elif contains_char(secret_string, guess_string[i]):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX

        i += 1

    return emoji_string


def input_guess(guess_int_len: int) -> str:
    """Prompts the user to enter the length of the guess word"""
    while True:
        guess = input(f"Enter a {guess_int_len} character word: ")
        # If the length of the guess word is the correct length, it will return the guess word
        if len(guess) == guess_int_len:
            return guess
        # If the guess word does not equal the length based on the user input, it will prompt the user to Try again
        else:
            print(f"That wasn't {guess_int_len} chars! Try again: ")


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turns: int = 1
    # Ensures the limit of turns <= 6 and does not create an infinite loop
    # Ensures user input "guess word" == length of the secret word
    # Prints the emojified function to display the hex code boxes based on conditions
    # If guess == secret, you will the game + return None
    # Otherwise, it continues to increment turns until the While loop terminates after 6 turns.
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(guess_int_len=len(secret))
        print(emojified(guess_string=guess, secret_string=secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            return None
        else:
            turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
