def transform(legacy_data):
    result = {}
    
    for point, letters in legacy_data.items():
        for letter in letters:
            if letter.lower() not in result:
                result[letter.lower()] = point
    
    return result
