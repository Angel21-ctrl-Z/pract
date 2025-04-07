import sys
sys.path.append('/home/angel21h/Development/pract/word_learning')

from Meaning.Functional_cat.Pronoun import Pronoun  # Importing the Pronoun class from the functional_cat module

word = Pronoun()  # Importing the Pronoun class from the Functional_cat module


def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    word.create()
    
    print("Word added successfully!\n")
    word.output()
    
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()