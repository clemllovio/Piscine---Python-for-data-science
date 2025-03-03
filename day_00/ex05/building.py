import sys
from string import punctuation


def main():
    try:
        if len(sys.argv) == 2:
            str = sys.argv[1]
        elif len(sys.argv) < 2:
            str = input("What is the text to count:\n")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")


        punctuation = "!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        upperLetter = 0
        lowerLetter = 0
        punctuationMarks = 0
        spaces = 0
        digits = 0

        for character in str:
            if character.islower():
                lowerLetter += 1
            elif character.isupper():
                upperLetter += 1
            elif character.isspace():
                spaces += 1
            elif character.isdigit():
                digits += 1
            elif character in punctuation:
                punctuationMarks += 1

        print("The text contains", len(str), "characters:")
        print(upperLetter, "upper letters")
        print(lowerLetter, "lower letters")
        print(punctuationMarks, "punctuation marks")
        print(spaces, "spaces")
        print(digits, "digits")

    except AssertionError as e:
        sys.stderr.write("AssertionError:", e)
    except KeyboardInterrupt:
        sys.stderr.write("Goodbye!")


if __name__ == "__main__":
    main()
