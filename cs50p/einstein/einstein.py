# get user input for mass and plug into convert fxn for joules
def get_mass():
    mass = float(input("Using Einsteins Theory of Relativity, I will convert a given mass (kg) to Energy in Joules: "))
    return mass

#use this to round only
mass = get_mass()
c =3 * (10**8)

E = round(mass * (c**2))

#use this to put a comma in the output number, no need for :, if you dont want it
print(f"{E:,} Joules")

