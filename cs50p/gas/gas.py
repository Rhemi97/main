def main():
    while True:
        try:
            fraction = input("Please input your gas remaining as a fraction: ")
            percentage = convert(fraction)

            if percentage > 100:
                print("Please input a valid gas remaining fraction: ")
                continue

            elif percentage >= 99:
                print("F")

            elif percentage <= 1:
                print("E")

            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            print("Please input a valid gas remaining fraction: ")

def convert(fraction):
    fraction = numerator, denomenator = map(int, fraction.split('/'))
    percentage = round(numerator / denomenator) * 100
    return percentage

main()







