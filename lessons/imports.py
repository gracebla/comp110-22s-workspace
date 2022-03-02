"""Examples of importing python."""


from lessons import helpers
from lessons import helpers as hp
# lets us use hp abbreviation instead of helpers.
from lessons.helpers import THE_ANSWER, powerful

# importing some module from some package


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(3, 3))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()