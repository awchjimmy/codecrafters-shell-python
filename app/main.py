import sys


def main():
    while True:
        cmd = input('$ ')
        if cmd != "exit":
            handle_command(cmd)
        else:
            break
    
def handle_command(cmd):
    print(f'{cmd}: command not found')


if __name__ == "__main__":
    main()
