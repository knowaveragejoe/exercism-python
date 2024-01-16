import string

def is_pangram(sentence):
    sentence = ''.join([char.lower() for char in sentence if char.isalpha()])
    unique_letters = []
    for char in sentence:
        if char not in unique_letters:
            unique_letters.append(char)
    
    unique_letters.sort()
    
    if unique_letters == list(string.ascii_lowercase):
        return True
    
    return False
    