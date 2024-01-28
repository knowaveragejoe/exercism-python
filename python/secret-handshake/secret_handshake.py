def commands(binary_str):
    binary = int(binary_str, 2)
    actions = []

    if binary & 0b1:
        actions.append("wink")
    
    if binary & 0b10:
        actions.append("double blink")
    
    if binary & 0b100:
        actions.append("close your eyes")
    
    if binary & 0b1000:
        actions.append("jump")
    
    if binary & 0b10000:
        actions.reverse()

    return actions