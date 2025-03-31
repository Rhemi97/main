def main():
    time = input("What time is it? ")  # Step 1: Get user input
    numeric_time = convert(time)  # Step 2: Convert to decimal

    # Step 3: Determine meal time
    if 7.0 <= numeric_time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= numeric_time <= 13.0:
        print("Lunch time")
    elif 18.0 <= numeric_time <= 19.0:
        print("Dinner time")

def convert(time):
    # Step 2a: Extract hours and minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Step 2b: Convert to decimal
    return hours + (minutes / 60)

# Step 6: Ensure the script runs properly
if __name__ == "__main__":
    main()
