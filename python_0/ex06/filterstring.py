import sys
from ft_filter import ft_filter


def main():
    # your test and your error handeling
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if sys.argv[1].isdigit() is not False:
            raise AssertionError("the arguments are bad")
        words = sys.argv[1].split()
        for word in words:
            if word.isalpha() is False:
                raise AssertionError("the arguments are bad")
        result = ft_filter(lambda x: len(x) >= int(sys.argv[2]), words)
        print(result)
    except Exception as e:
        print("AssertionError: ", e)


if __name__ == "__main__":
    main()
