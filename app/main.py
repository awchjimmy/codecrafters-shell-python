from doctest import OutputChecker
import os


def main():
    while True:
        user_input = input('$ ')
        if user_input != "exit":
            handle_command(user_input)
        else:
            break

def handle_command(user_input):
    parts = user_input.split(' ')
    cmd = parts[0]

    if cmd == "echo":
        line = ' '.join(parts[1:])
        print(line)
    elif cmd == "type":
        line = ' '.join(parts[1:])
        output = execute_type_command(line)
        print(output)

    else:
        print(f'{user_input}: command not found')



def execute_type_command(line):
    if line == "exit":
        output = "exit is a shell builtin"
    elif line == "echo":
        output = "echo is a shell builtin"
    elif line == "type":
        output = "type is a shell builtin"
    else:
        match = get_first_match_or_none(line)
        if match != None:
            output = f"{line} is {match}"
        else:
            output = f"{line}: not found"
    return output

def get_first_match_or_none(line):
    found = False
    output = ""
    paths = os.environ["PATH"].split(os.pathsep)
    for path in paths:
        full = f"{path}{os.sep}{line}"
        if os.access(full, os.X_OK):
            found = True
            output = full
    if found:
        return output
    else:
        return None


if __name__ == "__main__":
    main()
