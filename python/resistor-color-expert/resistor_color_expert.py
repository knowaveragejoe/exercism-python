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
        resistance = (first_digit * 10 + second_digit) * 10 ** third_digit

        tolerance = TOLERANCES[colors[3]]
    elif len(colors) == 5:
        fourth_digit = RESISTOR_COLOR_CODES[colors[3]]

        resistance = (first_digit * 100 + second_digit * 10 + third_digit) * 10 ** fourth_digit

        tolerance = TOLERANCES[colors[4]]

    tolerance_string = f"±{tolerance}%"

    if resistance < 1000:
        resistance_float = resistance
        ohms_string = "ohms"
        resistance_string = f"{resistance_float:.2f}".rstrip('0').rstrip('.') if '.' in f"{resistance_float:.2f}" else f"{resistance_float}"        
    elif resistance < 1000000:
        resistance_float = resistance / 1000
        ohms_string = "kiloohms"
        resistance_string = f"{resistance_float:.2f}".rstrip('0').rstrip('.') if '.' in f"{resistance_float:.2f}" else f"{resistance_float}"        
    elif resistance < 1000000000:
        resistance_float = resistance / 1000000
        ohms_string = "megaohms"
        resistance_string = f"{resistance_float:.2f}".rstrip('0').rstrip('.') if '.' in f"{resistance_float:.2f}" else f"{resistance_float}"        
    elif resistance < 1000000000000:
        resistance_float = resistance / 1000000000
        ohms_string = "gigaohms"
        resistance_string = f"{resistance_float:.2f}".rstrip('0').rstrip('.') if '.' in f"{resistance_float:.2f}" else f"{resistance_float}"        
    else:
        return "invalid resistance"

    return f"{resistance_string} {ohms_string} {tolerance_string}"