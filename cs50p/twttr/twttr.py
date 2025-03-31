def convert(text):
    converted_text = text.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return converted_text

def main():
    user_input = input("What would you like to say? " )
    converted_text = convert(user_input)
    print(converted_text)

main()
