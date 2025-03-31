class definition:
    def __init__(self):
        self.word = None
        self.meaning = None
        self.example = None

    def Create(self):
        self.word = input("Enter a new word: ")
        print(f"Word: {self.word}")
        self.meaning = input("Enter the meaning of the word: ")
        self.example = input("Enter an example sentence using the word: ")
        print(f"Meaning: {self.meaning}")
        print(f"Example: {self.example}")

if __name__ == "__main__":
    new_word = definition()
    new_word.Create()
    print(f"New word created: {new_word.word}, Meaning: {new_word.meaning}, Example: {new_word.example}")