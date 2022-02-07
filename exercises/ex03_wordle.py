"""EX03- Wordle exercise."""

__author__ = "730224294"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess: str, char: str) -> bool:
    """Returns true if the single character in guess is found at any index of secret."""
    a: int = (0)
    assert len(char) == 1
    while a < len(guess):
        if guess[a] == char:  
            return True
        else: 
            a += 1
    return False


def emojified(guess: str, secret: str) -> str: 
    """Returns string of emojis identifying correct characters in guess."""
    b: int = 0
    ans: str = " "
    assert len(guess) == len(secret)
    while b < len(secret):
        if guess[b] == secret[b]: 
            ans += GREEN_BOX
        elif contains_char(secret, guess[b]): 
            ans += YELLOW_BOX
        else: 
            ans += WHITE_BOX
        b += 1
    return ans


def input_guess(expected_len: int) -> str:
    """Asking user to input their charcater guess."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while len(guess) != (expected_len): 
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"   
    number_of_turns: int = 1
    result_of_game: bool = False
    while number_of_turns < 7 and result_of_game == False:
        print(f"=== Turn {number_of_turns} /6 === ")
        users_guess: str = input_guess(len(secret))
        print(emojified(users_guess, secret))
        if users_guess == secret: 
            result_of_game = True
            print(f"You won in {number_of_turns}/6 turns!")
        number_of_turns += 1
    if result_of_game == False: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
