import sys


def building(input_string: str):
    upper_letter = 0
    lower_letter = 0
    punctuation_mark = 0
    spaces = 0
    digits = 0

    for char in input_string:
        if char.isupper():
            upper_letter += 1
        elif char.islower():
            lower_letter += 1
        elif char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            punctuation_mark += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
    print(f"{upper_letter} upper letters")
    print(f"{lower_letter} lower letters")
    print(f"{punctuation_mark} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) == 1:
            input_string = input("input your string")
        elif len(sys.argv) == 2:
            input_string = sys.argv[1]
        else:
            raise AssertionError("more than onr argument is provided")
        building(input_string)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
