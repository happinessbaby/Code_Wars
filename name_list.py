def namelist(names):
    names = [i.get('name') for i in names]
    n = len(names)
    return {
    0: '',
    1:'{}',
    2:'{} & {}',
    3:'{}, '*(n-2) + '{} & {}'
    }[min(n, 3)].format(*names)

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
