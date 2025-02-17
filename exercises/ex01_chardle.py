"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730224294"


word_variable: str = input("Enter a 5-character word: ")

if len(word_variable) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter_variable: str = input("Enter a single character: ")

if len(letter_variable) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter_variable + " in " + word_variable)

if letter_variable == word_variable[0]: 
    print(letter_variable + " found at index 0")
if letter_variable == word_variable[1]: 
    print(letter_variable + " found at index 1")
if letter_variable == word_variable[2]: 
    print(letter_variable + " found at index 2")   
if letter_variable == word_variable[3]: 
    print(letter_variable + " found at index 3")     
if letter_variable == word_variable[4]: 
    print(letter_variable + " found at index 4")  
   

ans = word_variable.count(letter_variable)
if ans == 1:
    print(str(ans) + " instance of " + letter_variable + " found in " + word_variable)
else: 
    if ans > 1:
        print(str(ans) + " instances of " + letter_variable + " found in " + word_variable)
    else:
        print("No instances of " + letter_variable + " found in " + word_variable)
