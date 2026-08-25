import sys


def main():
    while True:
        cmd = input('$ ')
        handle_command(cmd)
    
def handle_command(cmd):
    print(f'{cmd}: command not found')


if __name__ == "__main__":
    main()
