#ask the user for input
def main():
    while True:
        try:
            fraction = input("Enter your remaining gas as a fraction: ")
            percentage = convert(fraction)

            if percentage > 100:
                print("Invalid input. Percentage cannot be greater than 100.")
                continue
            elif 99 <= percentage <= 100:
                print("F" )
            elif percentage <= 1:
                print("E")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError,):
            print ("Invalid input, please enter a valid fraction ")

def convert(fraction):
    fraction = numerator, denomenator = map(int, fraction.split('/'))  # Split fraction
    percentage = round(numerator / denomenator) * 100 # Convert to percentage
    return percentage

main()  # Run the program

