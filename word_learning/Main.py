from Meaning.definition import Definition

word = Definition()# This is a placeholder for the word object
                        # In real-world scenario, main will input the word.

def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    word.create()
    
    print("Word added successfully!\n")
    word.output()
    
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()