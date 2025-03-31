import random, math

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def get_coin():
  while True:
    try:
      get_coin = int(input("Please enter 25 cents: "))
      if get_coin == 25:
        print("Thanks, spinning.....")
        return
      else:
        print("Please insert exactly 25 cents: ")
    except ValueError:
      print("Please enter a valid amount: ")

def results(symbols):
  results = (random.choices(symbols, k=3))
  print(" | ".join(results))

  if results.count('7️⃣') == 3:
    print("You have won the Jackpot!")

  else:
    print("Thanks for playing, try again for a chance at the triple 7️⃣  jackpot!")

get_coin()
results(symbols)
