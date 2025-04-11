from Meaning.definition import Definition
import os

# This module is designed to handle lexical categories of words.
# It will include a class for lexical categories and methods to create and output them.

class LexicalCat(Definition):
    def __init__(self):
        super().__init__()
        self.lexical = None
        self.folder_path = os.path.join(os.path.dirname(__file__), "Lexical_cat")

    def create(self):
        super().create()
    
    def output(self):
        print(f"Category: {self.lexical}")
        super().output()
    
    def is_it(self):
        self.lexical = input("\nEnter the lexical category of the word: ").lower()
        print(f"Lexical: {self.lexical}")
        # Check if the lexical category is valid
        valid_categories = os.listdir(self.folder_path)
        valid_categories = [cat.lower() for cat in valid_categories if cat.endswith(".py") and cat != "__init__.py"]
        print(f"Valid categories: {valid_categories}")

        if self.lexical + ".py" in valid_categories:
            print(f"{self.lexical} is a valid lexical category.\n")
            return self.lexical
        else:
            print(f"{self.lexical} is not a valid lexical category.\n")
            self.lexical = None
            return None
    
    def get_lexical(self):
            self.make_list()
            if self.lexical in self.lexical_list:
                funcat_class = self.lexical_list[self.lexical]
                funcat = funcat_class()
                funcat.create()
            else:
                print(f"{self.function} is not a valid functional category.")
    
    def make_list(self):
        # This method will create a dictionary of functional categories from the folder
        self.lexical_list = {}
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove the ".py" extension
                try:
                    # Dynamically import the module and get the class
                    module = __import__(f"Meaning.Lexical_cat.{module_name}", fromlist=[module_name])
                    class_name = getattr(module, module_name.capitalize())
                    self.lexical_list[module_name.lower()] = class_name
                except (ImportError, AttributeError) as e:
                    print(f"Error importing {module_name}: {e}")
        return self.lexical_list
    
if __name__ == "__main__":
    new_lexical_cat = LexicalCat()
    new_lexical_cat.create()
    new_lexical_cat.output()