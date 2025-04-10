from Meaning.lexical_cat import LexicalCat

class Adverb(LexicalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.lexical = "adverb"

    def create(self):
        super().create()
        Adverb.mark(self)

    def mark(self):
        print(self.lexical)