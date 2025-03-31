import datetime

def main():
    months = [
    "January : 1",
    "February : 2",
    "March : 3",
    "April : 4",
    "May : 5",
    "June : 6",
    "July : 7",
    "August : 8",
    "September : 9",
    "October : 10",
    "November : 11",
    "December : 12"
]
#while loop to reprompt as necessary
while True:
    try:
        ui = input("Date: ")
        datetime.strptime({ui},'%m/%d/%Y').strftime('%Y-%m-%d')

    except ValueError:
        print("Please enter a valid date format: ")
        continue

    break

main()
