import sys


def morse(string):
    """ Receives a string and returns the morse code of it """

    if not string.replace(" ", "").isalnum() or len(string) == 0:
        raise AssertionError("AssertionError: The argument are bad")

    code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    string = string.upper()
    morse = ""
    for char in string:
        if char == " ":
            morse += " "
        else:
            morse += code[char] + " "

    print(morse)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: The arguments are bad")

        morse(sys.argv[1])

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
