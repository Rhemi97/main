import datetime

# Step 1: Get today's date
today = datetime.date.today()

# Step 2: Define next birthday using proper date format
next_bday = datetime.date(2026, 1, 18)

# Step 3: Calculate the difference
days_away = next_bday - today

if today == next_bday:
    print(random.choice(bday_messages))
else:
    print(f"Your next birthday is in {days_away.days} days!")
