memo = {}
def permutations(string, memo):
    if len(string) == 1:
        return string
    if len(string) == 2:
        return set([string, string[::-1]])
    if len(string) >= 3:
        memo.setdefault(string, [])
        for i in string:
            s = string.replace(i, '', 1)
            memo[string] += [i + p for p in permutations(s, memo)]
        return set(memo[string])


print(permutations('abcd', memo))


    #abcc: abcc, bcca, ccab, cabc, accb, acbc
    #abc: abc, acb, b
    #ac, bca, cab, cba
    #abcd:abcd,dabc, cdab, bcda, cabd, bcad, abcd, cabd,
