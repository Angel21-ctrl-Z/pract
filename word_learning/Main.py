import sys
sys.path.append('/home/angel21h/Development/pract/word_learning')
sys.path.append('/home/angel21v/Desktop/Development/pract/word_learning/Meaning')

import Meaning.functional_cat as functional_cat

word = functional_cat.FunctionalCat()


def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    word.is_it()
    word.get_function()
    
    print("Word added successfully!\n")
    word.output()
    
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()