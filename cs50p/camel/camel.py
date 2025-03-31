def convert(text):
    new_word = ""

    for char in text:
        if char.isupper():
            new_word += "_" + char.lower()  # Convert uppercase to lowercase with _
        else:
            new_word += char  # Keep lowercase letters as is

    return new_word.lstrip("_")  # Remove leading _ if the first letter was uppercase

def main():
    user_input = input("Enter a camelCase variable name: ")
    converted_text = convert(user_input)
    print("Snake case:", converted_text)

if __name__ == "__main__":
    main()
