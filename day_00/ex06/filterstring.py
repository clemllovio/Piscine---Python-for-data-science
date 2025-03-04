import sys
from ft_filter import ft_filter


def main():
    """
    This function processes command-line arguments to filter words from a given string
    based on their length.
    """
    try:
        assert len(sys.argv) == 3, "Wrong number of arguments"
        str = sys.argv[1]

        try:
            integer = int(sys.argv[2])
        except ValueError:
            raise AssertionError("argument is not an integer")

        assert any(c.isalpha() or c.isspace() for c in str), \
            "the argument are bad"
        str_split = str.split(' ')
        print(list(ft_filter(lambda x: (len(x) > integer), str_split)))

    except AssertionError as e:
        sys.stderr.write(f"AssertionError: {e}\n")


if __name__ == "__main__":
    main()
