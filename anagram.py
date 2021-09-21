
def anagrams(word, words):
    return list(i for i in words if sorted(i) == sorted(word))

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
