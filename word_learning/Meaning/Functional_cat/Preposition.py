from Meaning.functional_cat import FunctionalCat

class Preposition(FunctionalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.function = "preposition"

    def create(self):
        super().create()
        Preposition.mark(self)

    def mark(self):
        print(self.function)