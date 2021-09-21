
## better but still inefficient
def sum_pairs2(ints, s):
    ints = ints[::-1]
    pairs = []
    while len(ints) > 0:
        new_ele = ints.pop(0)
        if s - new_ele in ints:
            pairs.append([s-new_ele, new_ele])
    return pairs[-1] if pairs else None

def sum_pair3(ints, s):
    pairs = {}
    count = 0
    while len(ints) > 0:
        new_elem = ints.pop(0)
        count += 1
        if s - new_elem in ints[:int(len(ints)/4)]:
            #store the index of the second number
            pairs[ints.index(s-new_elem) + count] = [new_elem, s-new_elem]
            ints = ints[:int(len(ints)/4)]
        if s - new_elem in ints[int(len(ints)/2):]:
            pairs[ints.index(s-new_elem) + count] = [new_elem, s-new_elem]
            ints = ints[:ints.index(s-new_elem)]
    return pairs[sorted(pairs)[0]] if pairs else None

l1= [10, 5, 2, 3, 7, 5]
l2= [1, -2, 3, 0, -6, 1]
print(sum_pair3(l1, 10))
