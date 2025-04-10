import Meaning.functional_cat as functional_cat
import Meaning.lexical_cat as lexical_cat

add_function = functional_cat.FunctionalCat()
add_lexical = lexical_cat.LexicalCat()

def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    add_function.is_it()
    add_function.get_function()

    add_lexical.is_it()
    add_lexical.get_lexical()


    
    print("Word added successfully!\n")
    add_function.output()
    add_lexical.output()
    
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()