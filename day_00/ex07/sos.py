import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}


def main():
    """
    Encodes a string of letters into Morse code using a predefined dictionary.
    """
    encoded_char = []

    try:
        assert len(sys.argv) == 2, "the argument are bad(nbr)"

        for letter in sys.argv[1]:
            if letter.upper() in MORSE_CODE_DICT.keys():
                encoded_char.append(MORSE_CODE_DICT[letter.upper()])
            else:
                raise AssertionError("the argument are bad")
        encoded_str = ' '.join(encoded_char)
        print(encoded_str)
    except AssertionError as e:
        sys.stderr.write(f"AssertionError: {e}\n")


if __name__ == "__main__":
    main()
