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
    else:
        print(f'{user_input}: command not found')


if __name__ == "__main__":
    main()
