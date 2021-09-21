
def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < P:
        p0 = int(p0 + (percent/100) * p0 + aug)
        count += 1
    return count
