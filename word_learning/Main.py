from Meaning.Definition import definition


def main():
    print("Welcome to the Word Learning Program!")
    print("This program will help you learn new words and their meanings.")
    definition.Create(definition)
    
    print("Word added successfully!")
    print(f"Word: {definition.word} - Meaning: {definition.meaning} - Example: {definition.example}")
    print("Thank you for using the Word Learning Program!")

if __name__ == "__main__":
    main()