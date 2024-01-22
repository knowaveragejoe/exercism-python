def proverb(*input_data, **qualifier):    
    result = [f"For want of a {noun1} the {noun2} was lost." for noun1, noun2 in zip(input_data, input_data[1:])]
    
    if len(input_data) > 0:
        result.append(f"And all for the want of a {qualifier['qualifier']} {input_data[0]}.")
    
    return result