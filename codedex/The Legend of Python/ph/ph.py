def main():

    ph = int(input("Provide a value between 0-14: "))

    if ph < 7:
        print("Acidic")

    elif ph > 7:
        print("Basic")

    else:
        print("Neutral")

main()
