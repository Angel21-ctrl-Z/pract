import Meaning.functional_cat as functional_cat
import Meaning.lexical_cat as lexical_cat

add_function = functional_cat.FunctionalCat()
add_lexical = lexical_cat.LexicalCat()


def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    line = input("What would you like to do today? (Add a word, view words, exit): ").strip().lower()
    while True:
        if line == "add a word":
            print("Let's add a new word!\n")
            get_branches()
            print("Word added successfully!\n")
            add_function.output()
            add_lexical.output()

        elif line == "view words":
            print("Viewing words is not implemented yet.\n")
            
        elif line == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.")
        
        line = input("What would you like to do next? (Add a word, view words, exit): ").strip().lower()
    
    
    
    print("\nThank you for using the Word Learning Program!\n")

def get_branches():
    line = input("Is it a functional, lexical, or both category? (f/l/b): ").strip().lower()
    if line == "f":
        add_function.is_it()
        add_function.get_function()
    elif line == "l":
        add_lexical.is_it()
        add_lexical.get_lexical()
    elif line == "b":
        print("Adding both functional and lexical categories.\n")
        add_function.is_it()
        add_function.get_function()
        add_lexical.is_it()
        add_lexical.get_lexical()
    else:
        print("Invalid input. Please try again.")
    
if __name__ == "__main__":
    main()