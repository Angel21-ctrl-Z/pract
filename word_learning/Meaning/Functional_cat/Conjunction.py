from Meaning.functional_cat import FunctionalCat

class Conjunction(FunctionalCat):
    def __init__(self):
        super().__init__()
        self.type = None
        self.function = "conjunction"

    def create(self):
        super().create()
        Conjunction.mark(self)

    def mark(self):
        print(self.function)