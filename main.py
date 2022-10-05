from sys import argv
from rochi_utils import guess_random_int

if __name__ == "__main__":
    print(f'The __name__ from script is "{__name__}"')
    print(guess_random_int( argv[1] ))
