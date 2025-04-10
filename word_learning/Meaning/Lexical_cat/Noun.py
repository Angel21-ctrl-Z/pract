from Meaning.lexical_cat import LexicalCat

class Noun(LexicalCat):
    def __init__(self):
        super().__init__()
        self.lexical = "noun"
        self.type = None

    def create(self):
        super().create()
        Noun.mark(self)
        
    def mark(self):
        print(self.lexical)