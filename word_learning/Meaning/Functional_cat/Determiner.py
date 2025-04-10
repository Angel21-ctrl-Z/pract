from Meaning.functional_cat import FunctionalCat

class Determiner(FunctionalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.function = "determiner"

    def create(self):
        super().create()
        Determiner.mark(self)

    def mark(self):
        print(self.function)