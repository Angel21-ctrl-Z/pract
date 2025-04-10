from Meaning.functional_cat import FunctionalCat

class Pronoun(FunctionalCat):
    def __init__(self):
        super().__init__()
        self.function = "pronoun"
        self.type = None

    def create(self):
        super().create()
        Pronoun.mark(self)
        
    def mark(self):
        print(self.function)