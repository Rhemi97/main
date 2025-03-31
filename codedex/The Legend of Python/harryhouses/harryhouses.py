def main():
  houses = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
  }

  q1 = int(input("Do you like dawn or dusk?"))
  if q1 == 1:
    houses ["Gryffindor"] += 1
    houses ["Ravenclaw"] += 1
  elif q1 == 2:
    houses ["Hufflepuff"] += 1
    houses ["Slytherin"] += 1
  else:
    print("Wrong input: Dawn =1 and Dusk =2")

  q2 = int(input("When I'm dead, I want people to remember me as:"))
  if q2 == 1:
    houses ["Hufflepuff"] += 2
  elif q2 == 2:
    houses ["Slytherin"] += 2
  elif q2 == 3:
    houses ["Ravenclaw"] =+ 2
  elif q2 ==4:
    houses ["Gryffindor"] += 2
  else:
    print("Invalid input")

  q3 = int(input("What kind of instrument most pleases your ear?"))
  if q3 == 1:
    houses ["Slytherin"] += 4
  elif q3 == 2:
    houses ["Hufflepuff"] += 4
  elif q3 == 3:
    houses ["Ravenclaw"] += 4
  elif q3 ==4:
    houses ["Gryffindor"] += 4
  else:
    print("Invalid input")

  print("House points:", houses)

main()







