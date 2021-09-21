def unique_in_order(iterable):
    n = 0
    list = [iterable[n]]
    for i in range(1, len(iterable)):
        if iterable[i] != list[n]:
            list.append(iterable[i])
            n += 1
    return list

print(unique_in_order('AAAABBBCCDAABBB'))
