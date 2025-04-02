from definition import Definition
import os
import Functional_cat
# This module is designed to handle functional categories of words.
# It will include a class for functional categories and methods to create and output them.

class FunctionalCat(Definition):
    def __init__(self):
        super().__init__()
        self.function = None
        self.folder_path = "word_learning/Meaning/Functional_cat"

    def create(self):
        #self.function = is_it()
        super().create()
    
    def output(self):
        print(f"Function: {self.function}")
        super().output()
    
    def is_it(self):
        self.function = input("Enter the functional category of the word: ")
        print(f"Function: {self.function}")
        # Check if the functional category is valid
        valid_categories = os.listdir(self.folder_path)
        print(f"Valid categories: {valid_categories}")
        if self.function + ".py" in valid_categories:
            print(f"{self.function} is a valid functional category.")
        else:
            print(f"{self.function} is not a valid functional category.")
            self.function = None
    

if __name__ == "__main__":
    new_functional_cat = FunctionalCat()
    new_functional_cat.is_it()
    new_functional_cat.create()
    new_functional_cat.output()