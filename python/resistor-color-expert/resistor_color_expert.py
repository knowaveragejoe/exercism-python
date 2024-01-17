RESISTOR_COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}
    

def resistor_label(colors):
    if len(colors) == 1:
        return f"{RESISTOR_COLOR_CODES[colors[0]]} ohms"
    
    first_digit = RESISTOR_COLOR_CODES[colors[0]]
    second_digit = RESISTOR_COLOR_CODES[colors[1]]
    third_digit = RESISTOR_COLOR_CODES[colors[2]]
    
    # Determine tolerance usng multiplier if necessary
    if len(colors) == 4:    
        tolerance = TOLERANCES[colors[3]]
    elif len(colors) == 5:
        tolerance = TOLERANCES[colors[3]] * 10 ** TOLERANCES[colors[4]]
    
    resistance = (first_digit * 10 + second_digit) * 10 ** third_digit
    
    if resistance < 1000:
        return f"{resistance} ohms ±{tolerance}%"
    elif resistance < 1000000:
        return f"{resistance / 1000} kiloohms ±{tolerance}%"
    elif resistance < 1000000000:
        return f"{resistance / 1000000} megaohms ±{tolerance}%"
    elif resistance < 1000000000000:
        return f"{resistance / 1000000000} gigaohms ±{tolerance}%"
    else:
        return "Invalid resistance value"    
