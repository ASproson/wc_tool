def count_lines(lines):
    line_count = sum(1 for _ in lines)
    return line_count

def count_words(lines):
    word_count = sum(len(line.split()) for line in lines)
    return word_count

def count_chars(lines):
    char_count = sum(len(line) for line in lines)
    return char_count