import string

def is_isogram(word):
    letters = ''.join([char.lower() for char in word if char.isalpha()])
    return len(letters) == len(set(letters))
    