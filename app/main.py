from doctest import OutputChecker
import os
import subprocess

from app.helpers import is_executable
from app.execute_command import execute_type_command, execute_arbitrary_command, execute_pwd_command, execute_cd_command

def main():
    shared_app = {
        "current_dir": os.getcwd()
    }
    while True:
        user_input = input('$ ')
        if user_input != "exit":
            handle_command(user_input, shared_app)
        else:
            break

def handle_command(user_input, shared_app):
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
        output = execute_pwd_command(shared_app)
        print(output)
    elif cmd == "cd":
        execute_cd_command(shared_app, user_input)
    elif is_executable(cmd):
        output = execute_arbitrary_command(user_input)
        print(output.stdout, end="")
    else:
        print(f'{user_input}: command not found')

if __name__ == "__main__":
    main()
