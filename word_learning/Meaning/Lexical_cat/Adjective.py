from lexical_cat import LexicalCat
import os

# filepath: /home/angel21h/Development/pract/word_learning/Meaning/Lexical_cat/Adjective.py

class Adjective(LexicalCat):
    def __init__(self):
        super().__init__()
        self.type = None

    def describe(self):
        print(self.lexical)