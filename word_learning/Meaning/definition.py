class Definition:
    def __init__(self):
        self.word = None
        self.meaning = None
        self.example = None
        self.object = {}

# This method is used to create a new word and its meaning.
    # Once the Input is received, it will format the word and its meaning for output.
    def create(self):
        self.word = input("Enter a new word: ")
        
        self.meaning = input("Enter the meaning of the word: ")
        self.example = input("Enter an example sentence using the word: ")
        
        self.object = {self.word: {"meaning": self.meaning, "example": self.example}}

# This method is used to output the word, its meaning, and an example sentence.
    # Upon completion it will create a new word and its meaning.
    # It will also store the word in a dictionary.
    # This is a placeholder method and needs to be implemented.
    # In a real-world scenario, this would save the word to a database or a file.
    def output(self):
        if not self.word:
            print("No word has been created yet.")
            return
        print(f"\nWord: {self.object}")
        # Verify if the file exists, if not, create it and add the new word.
        file_path = "word_learning/Meaning/output/words.txt"

        try:
            with open(file_path, "a+") as file:
                file.seek(0)
                content = file.read()
                if self.word not in content:
                    file.write(f"{self.word}: {self.object[self.word]}\n")
                    print("\nWord added to the file.")
                else:
                    print("Word already exists in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")

# This method is used to check if the word is already in the dictionary.
    def is_it(self):
        pass
        

if __name__ == "__main__":
    new_word = Definition()
    new_word.create()
    new_word.output()