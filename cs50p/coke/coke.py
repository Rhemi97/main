def main():
    amount_due = 50 #coke price
    accepted_coins = [5, 10, 25]
    while amount_due > 0: #while loop that repeats until change is 0
        try:
            coin = int(input("Insert coin: "))
            if coin in accepted_coins:
                amount_due -= coin
            else:
                print("Invalid coin. Please insert 5, 10, 25: ")
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        except ValueError:
            print("Please enter a valid integer.")
        change_due = abs(amount_due)
        print(f"Change owed: {change_due}")

main()
