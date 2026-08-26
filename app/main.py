from doctest import OutputChecker
import os
import subprocess

from app.helpers import get_first_match_or_none, is_executable
from app.execute_command import execute_arbitrary_command

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
    elif cmd == "pwd":
        print(os.getcwd())
    elif is_executable(cmd):
        output = execute_arbitrary_command(user_input)
        print(output.stdout, end="")
    else:
        print(f'{user_input}: command not found')



def execute_type_command(line):
    if line == "exit":
        output = "exit is a shell builtin"
    elif line == "echo":
        output = "echo is a shell builtin"
    elif line == "type":
        output = "type is a shell builtin"
    elif line == "pwd":
        output = "pwd is a shell builtin"
    else:
        match = get_first_match_or_none(line)
        if match != None:
            output = f"{line} is {match}"
        else:
            output = f"{line}: not found"
    return output

if __name__ == "__main__":
    main()
