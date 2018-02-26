## Password Generator

I stumbled across a long list of words (~370k) and thought that I might try writing a password generator, inspired by 
the [xkcd classic](https://xkcd.com/936/).

It uses the [secrets](https://docs.python.org/3/library/secrets.html) library to select a user-selected number of words
from said long word list and (hand)craft a password from it.  (Isn't everything handcrafted nowadays?)

## Usage

Example usage: `python3 cli.py 5` will print a password made up of 5 randomly selected words.


I added an alias to my .bash_profile: `alias password='python3 /Path/To/Dir/cli.py'` to make it slightly easier to use.

## License
MIT License
