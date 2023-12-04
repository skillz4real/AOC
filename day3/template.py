def parse_lines(file):
    with open (file, 'r') as f:
        lines = f.readlines()
        return lines


if __name__ == "__main__":
    parse_lines('input.txt')
