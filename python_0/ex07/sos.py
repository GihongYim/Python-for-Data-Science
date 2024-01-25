import sys


def morse_code(line: str) -> list:
    """_summary_

    Args:
        line (str): string will be encoded with morse_code

    Returns:
        list: encoded string list
    """
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
    for char in sys.argv[1]:
        assert char.upper() in NESTED_MORSE.keys(), "the arguments are bad"
        char_list.append(NESTED_MORSE[char.upper()])
    encoded = " ".join(char_list)
    return encoded


def main():
    # your tests and your error handling
    """_summary_
    main_function for testing morse_code function
    """
    print(morse_code.__doc__)
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        encoded = morse_code(sys.argv[1])
        print(encoded)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
