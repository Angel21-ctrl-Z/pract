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

    def Output(self):
        print(f"Word: {self.word}")
        print(f"Meaning: {self.meaning}")
        print(f"Example: {self.example}\n")
    
    def is_it(self):
        pass
        

if __name__ == "__main__":
    new_word = definition()
    new_word.Create()
    new_word.Output()