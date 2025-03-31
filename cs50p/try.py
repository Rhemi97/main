# make a convert fxn and call
def convert(text):
    converted_text = text.replace(":)", "🙂").replace(":(", "☹️")
    return converted_text

# get user input
def main():
    user_input = input("Provide a smile or frown emoticon and I will turn it into an emoji" )
    converted_text = convert(user_input)
    print(converted_text)

if __name__ == "__main__":
    main()

