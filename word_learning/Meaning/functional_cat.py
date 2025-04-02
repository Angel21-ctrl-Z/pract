from definition import Definition
import os

# This module is designed to handle functional categories of words.
# It will include a class for functional categories and methods to create and output them.

class FunctionalCat(Definition):
    def __init__(self):
        super().__init__()
        self.function = None
        self.folder_path = "word_learning/Meaning/Functional_cat"

    def create(self):
        FunctionalCat.is_it(self)
        super().create()
    
    def output(self):
        print(f"Function: {self.function}")
        super().output()
    
    def is_it(self):
        self.function = input("Enter the functional category of the word: ").lower()
        print(f"Function: {self.function}")
        # Check if the functional category is valid
        valid_categories = os.listdir(self.folder_path)
        valid_categories = [cat.lower() for cat in valid_categories if cat.endswith(".py")]
        # Remove the ".py" extension from the valid categories
        print(f"Valid categories: {valid_categories}")
        if self.function + ".py" in valid_categories:
            print(f"{self.function} is a valid functional category.")
            return self.function
        else:
            print(f"{self.function} is not a valid functional category.")
            self.function = None
            return None
    

if __name__ == "__main__":
    new_functional_cat = FunctionalCat()
    new_functional_cat.create()
    new_functional_cat.output()