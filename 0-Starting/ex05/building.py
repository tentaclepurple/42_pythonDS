import sys
import string


def count_characters(text):
    if text is None or len(text) == 0:
        return ""

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace() or
                      char == "\n" or char == "\t" or char == "\r")

    total_chars = len(text)

    output = [
        f"The text contains {total_chars} characters:",
        f"{upper_count} upper letters",
        f"{lower_count} lower letters",
        f"{punctuation_count} punctuation marks",
        f"{space_count} spaces",
        f"{digit_count} digits"
    ]

    return "\n".join(output)


def main():
    if len(sys.argv) > 2:
        raise AssertionError("AssertionError: too many arguments")

    if len(sys.argv) == 1:
        try:
            text = input("What is the text to count?\n")
            text += "\n"
        except EOFError:
            text = ""

    else:
        text = sys.argv[1]

    result = count_characters(text)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(e)
