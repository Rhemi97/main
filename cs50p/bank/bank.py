x = input("Please start out conversation with a greeting ").lower().strip()

if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")

