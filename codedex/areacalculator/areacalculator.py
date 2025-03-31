shapes = ['Triangle, Square, Circle, Rectangle']

print("What shape would you like to calculae the area of?" )
print(shapes)
ui = input("").capitalize()

if ui == 'Triangle':
    base = float(input("What is base? "))
    height = float(input("What is height? "))
    area = (height * base)/2
elif ui == 'Square':
    side = float(input("What is the length of a side? " ))
    area = (side**2)
elif ui == 'Circle':
    raidus = float(input("What is the raidus? "))
    area = 3.14 * (raidus**2)
elif ui == 'Rectangle':
    length = float(input("What is the length? "))
    width = float(input("What is the width? "))
    area = length * width
else:
    print("Please enter a valid shape: ")

print(f"The area of your shape is: {area:.2f}")
