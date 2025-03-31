def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check overall length
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not starts_with_two_letters(s):
        return False

    # Ensure all characters are alphanumeric
    if not s.isalnum():
        return False

    digit_found = False
    for char in s:
        if char.isdigit():
            # Check if the first digit is '0'
            if not digit_found and char == '0':
                return False
            digit_found = True
        else:
            # If a letter appears after a digit has been found, it's invalid
            if digit_found:
                return False

    return True

def starts_with_two_letters(plate):
    # Ensure there are at least 2 characters
    if len(plate) < 2:
        return False
    # Return True only if the first two characters are letters
    return plate[0].isalpha() and plate[1].isalpha()

# Call main to run the program
main()
