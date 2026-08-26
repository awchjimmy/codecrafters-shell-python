
import subprocess

from app.helpers import get_first_match_or_none, is_executable

def execute_type_command(line):
    if line == "exit":
        output = "exit is a shell builtin"
    elif line == "echo":
        output = "echo is a shell builtin"
    elif line == "type":
        output = "type is a shell builtin"
    elif line == "pwd":
        output = "pwd is a shell builtin"
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
