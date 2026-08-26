
import subprocess
from pathlib import Path

from app.helpers import get_first_match_or_none, is_executable

def execute_echo_command(user_input):
    parts = user_input.split(' ')
    output = ' '.join(parts[1:])
    return output

def execute_type_command(user_input):
    parts = user_input.split(' ')
    line = ' '.join(parts[1:])
    if line == "exit":
        output = "exit is a shell builtin"
    elif line == "echo":
        output = "echo is a shell builtin"
    elif line == "type":
        output = "type is a shell builtin"
    elif line == "pwd":
        output = "pwd is a shell builtin"
    elif line == "cd":
        output = "cd is a shell builtin"
    elif is_executable(line):
        match = get_first_match_or_none(line)
        output = f"{line} is {match}"
    else:
        output = f"{line}: not found"
    return output

def execute_arbitrary_command(user_input):
    full_command = user_input.split(' ')
    output = subprocess.run(full_command, capture_output=True, text=True)
    return output

def execute_pwd_command(shared_app):
    return shared_app["current_dir"]

def execute_cd_command(shared_app, user_input):
    parts = user_input.split(' ')[1:]
    dest = ' '.join(parts)
    if Path(dest).exists():
        shared_app["current_dir"] = dest
    else:
        print(f"cd: {dest}: No such file or directory")
