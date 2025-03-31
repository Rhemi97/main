def main():
  distance = int(input("What is the distance in km? "))
  return distance

def distance_to_miles(distance):
  distance_to_miles = distance * 1.609
  print(distance_to_miles)

distance = main()
distance_to_miles(distance)
