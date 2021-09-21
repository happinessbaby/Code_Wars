import math
memo = {}
def permutation(string):
    if len(string) == 2:
        memo[string] = set([string, string[::-1]])
        return memo[string]
    memo.setdefault(string, set())
    for i in string:
        s = string.replace(i, '', 1)
        memo[string].update([i + p for p in permutation(s)])
    return memo[string]

def middle_permutation(string):
    P = permutation(''.join(string))
    P = sorted(P)
    return P[math.ceil(len(P)/2)-1]

print(middle_permutation('abcdxgz'))
