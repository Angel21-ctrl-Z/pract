import tomli

file_path = "/home/angel21v/Desktop/Development/pract/word_learning/pyproject.toml"

try:
    with open(file_path, "rb") as f:
        tomli.load(f)
    print("TOML syntax is valid.")
except Exception as e:
    print(f"TOML syntax error: {e}")