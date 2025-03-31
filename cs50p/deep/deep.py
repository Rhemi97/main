answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip()

match answer:
    case "42" | " 42 " | "Forty Two" | "forty-two" | "FoRty TwO" | "forty two":
        print("Yes")
    case _:
        print("No")

