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


def label(colors):
    first_digit = RESISTOR_COLOR_CODES[colors[0]]
    second_digit = RESISTOR_COLOR_CODES[colors[1]]
    third_digit = RESISTOR_COLOR_CODES[colors[2]]
    
    resistance = int((first_digit * 10 + second_digit) * 10 ** third_digit)
    
    if resistance < 1000:
        return f"{resistance:.0f} ohms"
    elif resistance < 1000000:
        return f"{resistance / 1000:.0f} kiloohms"
    elif resistance < 1000000000:
        return f"{resistance / 1000000:.0f} megaohms"
    elif resistance < 1000000000000:
        return f"{resistance / 1000000000:.0f} gigaohms"
    else:
        return "Invalid resistance value"    
    
