

def validBraces(string):
    x = []
    open = ['(', '[', '{']
    close = [')', ']', '}']
    for i in range(len(string)):
        if string[i] in open:
            x.append(close[open.index(string[i])])
        if string[i] in close:
            if len(x) == 0 and len(string) != 0: #extra closing braces
                return False
            elif string[i] != x[-1]: #braces in wrong order
                return False
            else:
                x.pop()
    #extra opening braces
    if len(x) != 0:
        return False
    return True


print(validBraces("{[()]}()"))
