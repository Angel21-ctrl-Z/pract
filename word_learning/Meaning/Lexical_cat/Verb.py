from Meaning.lexical_cat import LexicalCat
import os

# filepath: /home/angel21v/Desktop/Development/pract/word_learning/Meaning/Lexical_cat/Verb.py

class Verb(LexicalCat):
    def __init__(self):
        super().__init__()
        self.type = None

    def modify(self):
        print(self.lexical)