from os import path
from pickle import load
import secrets

DIR_PATH = path.dirname(path.abspath(__file__))


class Password:

    def __init__(self, num_words):
        """
        :param num_words: int, number of words to be chosen from the word list.
        """
        self.num_words = num_words
        self.words = self.load_words()
        self.password = self.generate_password()

    def __repr__(self):
        return f'Password({self.num_words})'
    
    def __str__(self):
        return f'Password object created with {self.num_words} randomly chosen words'

    def __len__(self):
        return len(self.password)

    @staticmethod
    def load_words():
        with open(path.join(DIR_PATH, 'word_dict'), 'rb') as file:
            return load(file)

    def get_num_words(self):
        return self.num_words

    def generate_password(self):
        password = []
        for i in range(self.num_words):
            password.append(secrets.choice(self.words))
        return ' '.join(password)

    def set_num_words(self, num):
        self.num_words = num

    def get_words(self):
        return dict(self.words)

    def get_password(self):
        return self.password[:]

