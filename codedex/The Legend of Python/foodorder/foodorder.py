food = ['Cheeseburger', 'Karaage', 'Sushi', 'Katsudon', 'Gyudon', 'Omurice', 'Onigiri']

def get_order():
    order = int(input("What would you like to order (1 - 7)? "))
    return food[order - 1]

print(get_order())
