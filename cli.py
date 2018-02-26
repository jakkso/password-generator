from argparse import ArgumentParser as Ag

from classes import Password


def main():
    parser = Ag()
    parser.add_argument('length', help='Desired number of words, must be an integer')
    args = parser.parse_args()
    try:
        print(Password(int(args.length)).get_password())
    except ValueError:
        parser.print_help()


if __name__ == '__main__':
    main()
