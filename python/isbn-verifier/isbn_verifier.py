def is_valid(isbn):    
    isbn = isbn.replace("-", "")
    digits = list(isbn[:10])
    
    if len(isbn) != 10:
        return False
    
    # Check all remaining characters are digits up to check digit
    if not all(digit.isnumeric() for digit in digits[:8]):
        return False
    
    # Replace check digit with 10 if necessary
    if digits[-1].isalpha():
        if digits[-1] == "X":
            digits[-1] = 10
        else:
            return False
    
    # Convert to ints
    digits = [int(digit) for digit in digits]

    # Perform the check
    sum = 0
    mult = 10
    for i in digits[::-1]:
        sum += i * mult
        mult -= 1

    if sum % 11 == 0:
        return True
    
    return False
