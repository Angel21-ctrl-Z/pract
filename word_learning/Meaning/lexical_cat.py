from definition import Definition
import os

# This module is designed to handle lexical categories of words.
# It will include a class for lexical categories and methods to create and output them.

class LexicalCat(Definition):
    def __init__(self):
        super().__init__()
        self.lexical = None
        self.folder_path = "word_learning/Meaning/Lexical_cat"

    def create(self):
        LexicalCat.is_it(self)
        super().create()
    
    def output(self):
        print(f"Category: {self.lexical}")
        super().output()
    
    def is_it(self):
        self.lexical = input("Enter the lexical category of the word: ").lower()
        print(f"Lexical: {self.lexical}")
        # Check if the lexical category is valid
        valid_categories = os.listdir(self.folder_path)
        valid_categories = [cat.lower() for cat in valid_categories if cat.endswith(".py")]
        print(f"Valid categories: {valid_categories}")

        if self.lexical + ".py" in valid_categories:
            print(f"{self.lexical} is a valid lexical category.")
            return self.lexical
        else:
            print(f"{self.lexical} is not a valid lexical category.")
            self.lexical = None
            return None
    
    
if __name__ == "__main__":
    new_lexical_cat = LexicalCat()
    new_lexical_cat.create()
    new_lexical_cat.output()