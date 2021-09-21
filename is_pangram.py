import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    letters = set(s)
    return letters.issuperset(alphabet)
