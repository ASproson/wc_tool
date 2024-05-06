import argparse
import sys
from utils import count_lines, count_words, count_chars

def main():
    parser = argparse.ArgumentParser(prog="ccwc.py", description="Unix word counter", usage="[program] [file] [options]")
    parser.add_argument('filename', nargs='?', help="Input file")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--lines", action='store_true', help="Count the number of lines")
    group.add_argument("-w", "--words", action='store_true', help="Count the number of words")
    group.add_argument("-m", "--characters", action='store_true', help="Count the number of characters")

    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    if not (args.lines or args.words or args.characters):
        line_count = count_lines(lines)
        word_count = count_words(lines)
        char_count = count_chars(lines)
        filename_str = f" {args.filename}" if args.filename else ""
        print(f"{line_count} {word_count} {char_count} {filename_str}")
    else:
        if args.lines:
            line_count = count_lines(lines)
            print(f"Number of lines: {line_count}")

        if args.words:
            word_count = count_words(lines)
            print(f"Number of words: {word_count}")

        if args.characters:
            char_count = count_chars(lines)
            print(f"Number of characters: {char_count}")

if __name__ == "__main__":
    main()


# cat test.txt | python ccwc.py -l
# python ccwc.py test.txt
# python ccwc.py test.txt -w