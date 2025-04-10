from Meaning.lexical_cat import LexicalCat

class Adjective(LexicalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.lexical = "adjective"

    def create(self):
        super().create()
        Adjective.mark(self)

    def mark(self):
        print(self.lexical)