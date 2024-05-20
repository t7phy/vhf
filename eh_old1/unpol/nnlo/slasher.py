import sys

def add_slash_to_lines(filename, start_line, end_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i, line in enumerate(lines):
            if start_line <= i+1 <= end_line:
                if line.endswith(';\n'):
                    line = line.rstrip(';\n') + '\n'
                elif not line.endswith('\\\n'):
                    line = line.rstrip('\n') + '\\' + '\n'
                file.write(line)
            else:
                file.write(line)

if __name__ == "__main__":
    filename = sys.argv[1]
    start_line = int(sys.argv[2])
    end_line = int(sys.argv[3])
    add_slash_to_lines(filename, start_line, end_line)