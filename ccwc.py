import argparse

def count_lines(filename):
  with open(filename, 'r') as file:
    line_count = sum(1 for _ in file)
  return line_count

def main():
  parser = argparse.ArgumentParser(prog="ccwc.py", description="Unix word counter", usage="[program] [file] [options]")
  parser.add_argument('filename', help="Input file")
  parser.add_argument("-l", "--lines", action='store_true', help="Count lines in the specified file")
  args = parser.parse_args()

  file = args.filename

  if args.lines:
    line_count = count_lines(file)
    print(f"Number of lines {file}: {line_count}")

if __name__ == "__main__":
  main()