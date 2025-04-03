from definition import Definition
import os
import Functional_cat # This is a module for functional categories of words.


# This module is designed to handle functional categories of words.
# It will include a class for functional categories and methods to create and output them.

class FunctionalCat(Definition):
    def __init__(self):
        super().__init__()
        self.function = None
        self.folder_path = "word_learning/Meaning/Functional_cat"
        self.function_list = {}

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
        print(f"Valid categories: {valid_categories}")

        if self.function + ".py" in valid_categories:
            print(f"{self.function} is a valid functional category.")
            return self.function
        else:
            print(f"{self.function} is not a valid functional category.")
            self.function = None
            return None
    
    def get_function(self):
        self.make_list()
        if self.function in self.function_list:
            funcat_class = self.function_list[self.function]
            funcat = funcat_class()
            funcat.mark()
        else:
            print(f"{self.function} is not a valid functional category.")
        
        print(f"Functional category: {funcat}")

    def make_list(self):
        # This method will create a dictionary of functional categories from the folder
        self.function_list = {}
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove the ".py" extension
                try:
                    # Dynamically import the module and get the class
                    module = __import__(f"Functional_cat.{module_name}", fromlist=[module_name])
                    class_name = getattr(module, module_name.capitalize())  # Assume class name matches the file name
                    self.function_list[module_name.lower()] = class_name
                except (ImportError, AttributeError) as e:
                    print(f"Error importing {module_name}: {e}")
        return self.function_list

if __name__ == "__main__":
    new_functional_cat = FunctionalCat()
    new_functional_cat.create()
    new_functional_cat.output()
    new_functional_cat.get_function()