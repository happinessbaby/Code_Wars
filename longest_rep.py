import string

repetition = {}
memo = {}
def get_repetitions(s, index):
    if index >= len(s) - 1:
        repetition.setdefault(index, 1)
        return 1
    elif s[index] == s[index + 1]:
        memo[index] = 1 + get_repetitions(s, index+1)
        repetition.setdefault(index, memo[index])
        return memo[index]
    else:
        memo[index] = min(1, get_repetitions(s, index+1))
        repetition.setdefault(index, memo[index])
        return memo[index]

def longest_repetition(s):
    get_repetitions(s.lower(), 0) # 0 is the starting index of the string
    values = list(repetition.values())
    keys = list(repetition.keys())
    return (s[keys[values.index(max(values))]].lower(),max(values))

print(longest_repetition("""Bababadalgharaghtakamminarronnkonnbronntonnerronn
tuonnthunntrovarrhounawnskawnto"""))
