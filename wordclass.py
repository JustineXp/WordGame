import random
from words import words


class Word:
    def __init__(self):
        self.random_word = ''
        self.first_letter = ''
        self.word_list = []
        self.random_word_generator()
        self.allwords()

    def __repr__(self):
        return self.random_word

    def random_word_generator(self):
        random_word = random.choice(words)
        self.random_word = random_word['word']
        self.first_letter = random_word['word'][0].upper()

    def allwords(self):
        self.word_list = [word['word']
                          for word in words if self.first_letter == word['word'][0].upper()]
