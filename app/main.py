import sys


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
        output = f"{line}: not found"
    return output


if __name__ == "__main__":
    main()
