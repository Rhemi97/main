def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0  # Initialize total

    while True:
        try:
            ui = input("Item: ").casefold().title()  # Make input case-insensitive

        except KeyError:
            pass

        except EOFError:  # Handle Ctrl+D (EOF)
            print(f"\nTotal: ${total:.2f}")
            break  # Exit program

        if ui in menu:
            price = menu[ui]  # Get item price
            total += price  # Update total
            print(f"Total: ${total:.2f}")  # Display total

main()




