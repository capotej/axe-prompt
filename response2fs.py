import os
import sys

def parse_txtar(input_data):
    lines = input_data.splitlines()
    current_file = None
    current_content = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("-- ") and stripped_line.endswith(" --"):
            if current_file:
                write_file(current_file, current_content)
                current_content = []
            current_file = stripped_line[3:-3].strip()
        elif current_file:
            current_content.append(line)

    if current_file:
        write_file(current_file, current_content)

def write_file(filename, content):
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(filename, 'w') as file:
        file.write('\n'.join(content))

def main():
    input_data = sys.stdin.read()
    parse_txtar(input_data)

if __name__ == "__main__":
    main()

