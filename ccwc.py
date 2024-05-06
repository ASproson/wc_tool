import argparse

def main():
  parser = argparse.ArgumentParser(prog="ccwc.py", description="Unix word counter", usage="program [options] STRING")
  parser.add_argument('string', metavar="STRING", type=str, help="Input string")
  args = parser.parse_args()

  input_string = args.string
  string_length = len(input_string)

  print(f"Input string: {input_string}")
  print(f"Length: {string_length}")

if __name__ == "__main__":
  main()