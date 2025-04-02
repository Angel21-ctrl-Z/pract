import os

def list_folder_to_string(folder_path):
#Lists the contents of a folder and returns them as a string, with each item separated by a newline.
  try:
    items = os.listdir(folder_path)
    return items
  except FileNotFoundError:
    return f"Error: Folder '{folder_path}' not found."
  except NotADirectoryError:
      return f"Error: '{folder_path}' is not a valid directory."
  except Exception as e:
      return f"An error occurred: {e}"

# Example usage:
#folder_path = "word_learning/Meaning/Functional_cat"  # Replace with the actual path to your folder
#folder_string = list_folder_to_string(folder_path)
#print(folder_string)
