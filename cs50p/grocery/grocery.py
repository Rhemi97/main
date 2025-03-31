def main():
    grocery_list = {}

    while True:
        try:
            ui = input("").strip().upper()

            if ui in grocery_list:
                grocery_list[ui] += 1
            else:
                grocery_list[ui] = 1

        except EOFError:
            for item in sorted(grocery_list):
                print(grocery_list[item], item)
            break

main()
