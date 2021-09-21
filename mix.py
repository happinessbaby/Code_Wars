import string
from collections import Counter
import functools

def mix(s1, s2):
    alphabet = string.ascii_lowercase
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    for i in range(len(s1)):
        if s1[i] in alphabet:
            s1 = s1[i:]
            break
    for i in range(len(s2)):
        if s2[i] in alphabet:
            s2 = s2[i:]
            break
    d1 = Counter(s1)
    D1 = [num for num in list(d1.items()) if num[1] != 1]
    d2 = Counter(s2)
    D2 = [num for num in list(d2.items()) if num[1] != 1]
    max_counts = sorted(dict(d1 | d2).items(), key=lambda x:x[1], reverse= True)
    max_counts = [num for num in max_counts if num[1] != 1]
    S = functools.reduce(lambda y, i: y + {
    1: '1:'+ max_counts[i][0]*max_counts[i][1] +'/', #if item in d1
    2: '2:'+ max_counts[i][0]*max_counts[i][1] +'/', #if item in d2
    3: '=:' + max_counts[i][0]*max_counts[i][1] + '/', # if item in both
    }[check_counts(max_counts, i, D1, D2)].format(*max_counts[i]),
    range(len(max_counts)), '')[:-1]
    return '/'.join(sorted(sorted(sorted(S.split('/'), key = lambda s:s[2]), key=lambda s: s[0]), key=lambda s: len(s), reverse = True)) if len(max_counts) > 0 else ''

def check_counts(max_counts, i, D1, D2):
    if max_counts[i] in D1 and max_counts[i] not in D2:
        return 1
    elif max_counts[i] in D2 and max_counts[i] not in D1:
        return 2
    else:
        return 3


print(mix("codewars", "codewars"))
