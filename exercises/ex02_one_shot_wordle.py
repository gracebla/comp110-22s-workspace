"""EX02- Wordle exercise."""

__author__ = "730224294"

from numpy import char


secret: str = ("python")
guess: str = input("What is your 6-letter guess? ")
first: str = guess[0]

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
a: int = (0)
character_in_guess: str = (guess[a]) 


if len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")    

if len(guess) == len(secret):
    while guess != secret and a < len(secret):
        if guess[a] == secret[a]: 
            print(GREEN_BOX)   
        else:
            while fit == False:

            else: 
                print(WHITE_BOX)
        a = a + 1
print("Not quite. Play again soon!")
(exit)
if guess == secret:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")   
