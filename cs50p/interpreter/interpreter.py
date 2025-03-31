#asking for the input
expression = input("Enter an expression: ").strip()

x, operator, y = expression.split(" ")

x = float(x)
y = float(y)

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "/":
    result = x / y
elif operator == "*":
    result = x * y
else:
    print("Invalid Operator")
    exit()

#use this to put a comma in the output number, no need for :, if you dont want it
print(f"{result:.1f}")
