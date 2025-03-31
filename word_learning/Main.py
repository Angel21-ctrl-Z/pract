from Meaning.Definition import definition

word = definition()

def main():
    print("\nWelcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.\n")
    word.Create()
    
    print("Word added successfully!\n")
    word.Output()
    
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()