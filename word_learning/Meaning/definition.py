class Definition:
    def __init__(self):
        self.word = None # Main word object
        # This is a placeholder for the word object.
        self.meaning = None
        self.example = None

# This method is used to create a new word and its meaning.
    # Once the Input is received, it will format the word and its meaning for output.
    def create(self):
        self.word = input("Enter a new word: ")# This line will be edit out to main.
        print(f"Word: {self.word}")
        
        self.meaning = input("Enter the meaning of the word: ")
        self.example = input("Enter an example sentence using the word: ")
        print(f"Meaning: {self.meaning}")
        print(f"Example: {self.example}")

# This method is used to output the word, its meaning, and an example sentence.
    # Upon completion it will create a new word and its meaning.
    # It will also store the word in a dictionary.
    # This is a placeholder method and needs to be implemented.
    # In a real-world scenario, this would save the word to a database or a file.
    def output(self):
        print(f"Word: {self.word}")
        print(f"Meaning: {self.meaning}")
        print(f"Example: {self.example}\n")

# This method is used to check if the word is already in the dictionary.
    # This is a placeholder method and needs to be implemented.
    # In a real-world scenario, this would check against a database or a file.
    def is_it(self):
        pass
        

if __name__ == "__main__":
    new_word = Definition()
    new_word.create()
    new_word.output()