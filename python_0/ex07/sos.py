import sys


def main():
    # your tests and your error handling
    """main function for morse """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ', ': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '/': '-..-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-'
    }
    char_list = []
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    for char in sys.argv[1]:
        if char.upper() not in NESTED_MORSE.keys():
            raise AssertionError("the arguments are bad")
        char_list.append(NESTED_MORSE[char.upper()])
    encoded = " ".join(char_list)
    print(encoded)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("AssertionError: ", e)
