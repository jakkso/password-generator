from os import path
from pickle import dump

DIR_PATH = path.dirname(path.abspath(__file__))


def create_dict(dict_name):
    """
    Creates a pickled dict of all the words in words_alpha.txt
    :return: None
    """
    # Open text file, make a list of it
    with open(path.join(DIR_PATH, 'words_alpha.txt')) as file:
        words = [item.strip() for item in file]
    # Make a dict of the items in the list, with the keys being the enumerate()
    # value of each item, and the word being the value
    d = {num: word for num, word in enumerate(words)}
    # Save the dict via pickle
    with open(path.join(DIR_PATH, dict_name), 'wb') as file:
        dump(d, file)
