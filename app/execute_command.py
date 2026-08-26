
import subprocess


def execute_arbitrary_command(user_input):
    full_command = user_input.split(' ')
    output = subprocess.run(full_command, capture_output=True, text=True)
    return output
