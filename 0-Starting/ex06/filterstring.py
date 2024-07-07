from ft_filter import ft_filter
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: The \
                arguments are bad")
        string = sys.argv[1]

        try:
            num = int(sys.argv[2])

        except ValueError:
            raise AssertionError("AssertionError: Second argument \
                must be an integer")

        result = [item for item in ft_filter(lambda x: len(x)
                                             > num, string.split())]

        print(result)

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
