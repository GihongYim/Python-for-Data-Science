import sys
import string
def main():
    # your tests and your error handling
    try:
        if len(sys.argv) > 2:
            raise AssertionError("argv is more than expected")
    except AssertionError as e:
        print("AssertiongError: ", e)
        return 
    sentence = ""
    if len(sys.argv) == 1:
        sentence = input("What is the text to count?\n")
    else:
        sentence = sys.argv[1]
    count = {
        "lower_letter" : 0, 
        "upper_letter" : 0, 
        "punctuation_mark" : 0,
        "spaces" : 0,
        "digits" : 0
        }
    for char in sentence:
        if char.islower():
            count["lower_letter"] += 1
        elif char.isupper():
            count["upper_letter"] += 1
        elif char in string.punctuation:
            count["punctuation_mark"] += 1
        elif char == " ":
            count["spaces"] += 1
        elif char.isdigit():
            count["digits"] += 1
    print("{} upper letters".format(count["upper_letter"]))
    print("{} lower letters".format(count["lower_letter"]))
    print("{} functuation marks".format(count["punctuation_mark"]))
    print("{} spaces".format(count["spaces"]))
    print("{} digits".format(count["digits"]))

if __name__ == "__main__":
    main()