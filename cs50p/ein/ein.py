#prompt user for a mass
def get_mass():
    mass = (float(input("Give me mass for einstein eq: ")))
    return mass

#start the equations
mass = get_mass()

c= 3 * (10**8)

E = round(mass * (c**2))

print(f{E:, })
