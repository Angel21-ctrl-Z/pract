from Meaning.lexical_cat import LexicalCat

class Verb(LexicalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.lexical = "verb"

    def create(self):
        super().create()
        Verb.mark(self)

    def mark(self):
        print(self.lexical)