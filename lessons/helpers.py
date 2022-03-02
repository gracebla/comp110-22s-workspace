"""Demonstrate defining a module imported elsewhere."""

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n 


# idiom for making a module able to run as a program
if __name__ == "__main__":
    main()
else:
    # we typically do not have an else branch here, just for demonstration
    print(f"helpers.py was imported: {__name__}")