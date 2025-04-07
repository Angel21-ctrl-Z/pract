from Meaning.functional_cat import FunctionalCat
import os

class Preposition(FunctionalCat):
    def __init__(self):
        super().__init__()
        self.type = None

    def mark(self):
        print(self.function)