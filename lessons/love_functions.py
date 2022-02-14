"""Some examples of tender, loving function definitions."""

name: str = input("Enter a name:")   


def love(name: str) -> str: 
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"
    # f string makes it so you do not have to concatenate"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note = love_note + love(to) + "\n"
        counter += 1 
    return love_note


print(spread_love("Grace", 4))