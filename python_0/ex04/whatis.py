import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
