from itertools import product


def main() -> None:
    DIGITS = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    OPERATORS = ["+", "-", ""]

    for ops in product(OPERATORS, repeat=len(DIGITS) - 1):
        expression = "".join(d + o for d, o in zip(DIGITS, ops)) + DIGITS[-1]
        if eval(expression) == 200:
            print(expression)


if __name__ == "__main__":
    main()
