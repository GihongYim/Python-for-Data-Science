import sys

from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, " the arguments are bad"
        assert sys.argv[2].isnumeric(), " the arguments are bad"
        s = sys.argv[1]
        n = int(sys.argv[2])
        words = ft_filter(lambda x: len(x) > n, s.split())
        result = [word for word in words]
        print(result)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return


if __name__ == "__main__":
    main()
