import random

bday_messages = [
'Hope you have a very Happy Birthday! 🎈',
'Its your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞'
]

def random_message():
  print(random.choice(bday_messages))

random_message()
