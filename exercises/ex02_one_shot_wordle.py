"""EX02- Wordle exercise."""

__author__ = "730224294"

secret: str = ("python")
guess: str = input("What is your 6-letter guess? ")
a: int = (0)
# assign answer as an empty string so you can add things to it
answer: str = ("")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")    

if len(guess) == len(secret):
    while a < len(secret):
        if guess[a] == secret[a]: 
            # reassign answer variable so you can add boxes as a str
            answer = answer + GREEN_BOX  
        else:
            # assign new variable "b" so you do not interfere with variable "a"
            b: int = (0)
            guess_included: bool = False
            while not guess_included and b < len(guess):
                if secret[b] == guess[a]:
                    guess_included = True
                b = b + 1
            if guess_included: 
                answer = answer + YELLOW_BOX
            else: 
                answer = answer + WHITE_BOX    
        a = a + 1
    print(answer)    

if guess == secret:
    print("Woo! You got it!")   
else: 
    print("Not quite. Play again soon!")

    