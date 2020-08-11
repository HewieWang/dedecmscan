from termcolor import cprint
from lib.lib import check

def main():
    target = input("Please enter the url you need to detect: ")
    start = check(target)
    start.poc()

if __name__ == '__main__':
    main()
