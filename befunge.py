import random

num = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
oper = ['+', '-', '*', '/', '%', '`']
dir = ['^', 'v', '<', '>']
change_dir = ['?', '|', '_']
outputs = [',','.']
misc = ['!','$','\\', ':', ' ', 'g']

def interpret(code):
    grid, stack, output = [], [], ''
    grid = append_grid(grid, code)
    row, col, current_dir = 0, 0, '>'
    while True:
        x = grid[row][col][0]
        if x =='@':
            break
        if x in outputs:
            [stack, output] = get_output(stack, output, x)
            [current_dir, row, col] = directions(current_dir, row, col)
        if x in num or x in oper or x in misc:
            stack = actions(grid, stack, x)
            [current_dir, row, col] = directions(current_dir, row, col)
        if x in dir:
            [current_dir, row, col] = directions(x, row, col)
        if x in change_dir:
            [stack, current_dir] = change_directions(stack, x)
            [current_dir, row, col] = directions(current_dir, row, col)
        if x == '"':
            [stack, current_dir, row, col] = string_mode(grid, stack, x, current_dir, row, col)
        if x == '#':
            [current_dir, row, col] = directions(current_dir, row, col)
            [current_dir, row, col] = directions(current_dir, row, col)
        if x == 'p':
            x_cor = stack.pop()
            y_cor = stack.pop()
            v = stack.pop()
            grid[x_cor][y_cor][0] = chr(v)
            [current_dir, row, col] = directions(current_dir, row, col)
    return output

def directions(x, row, col):
    if x == '^':
        return ['^', row-1, col]
    if x == 'v':
        return ['v', row+1, col]
    if x == '>':
        return ['>', row, col+1]
    if x == '<':
        return ['<', row, col-1]

def change_directions(stack, x):
    if x == '?':
        return [stack, random.choice('v^<>')]
    if x == '_':
        return [stack, '>'] if stack.pop() == 0 else [stack,'<']
    if x == '|':
        return [stack,'v'] if stack.pop() == 0 else [stack,'^']

def string_mode(grid, stack, x, current_dir, row, col):
    while True:
        [current_dir, row, col] = directions(current_dir, row, col)
        x = grid[row][col][0]
        if x == '"':
            [current_dir, row, col] = directions(current_dir, row, col)
            return [stack, current_dir, row, col]
        else:
            stack.append(ord(x))

def get_output(stack, output, x):
    if x == '.':
        output += str(stack.pop())
    if x == ',':
        output += chr(stack.pop())
    return [stack, output]

def actions(grid, stack, x):
    if x in num:
        stack.append(int(x))
    if x in oper:
        stack = operations(stack, x)
    if x == '!':
        stack.append(1 if stack.pop()== 0 else 0)
    if x == '$':
        stack.pop()
    if x == ' ':
        return stack
    if x == '\\':
        if len(stack) == 1:
            stack.append(0)
        else:
            temp = stack[-1]
            stack[-1] = stack[-2]
            stack[-2] = temp
    if x == ':':
        if stack == []:
             stack.append(0)
        else:
            stack.append(stack[-1])
    if x == 'g':
        x_cor = stack.pop()
        y_cor = stack.pop()
        try:
            stack.append(ord(grid[x_cor][y_cor][0]))
        except IndexError:
            stack.append(0)
    return stack

def operations(stack, x):
    a = stack.pop()
    b = stack.pop()
    if x == '+':
        stack.append(a + b)
    if x == '-':
        stack.append(b - a)
    if x == '*':
        stack.append(a*b)
    if x == '/':
        stack.append(b/a if a != 0 else 0)
    if x == '%':
        stack.append(b%a if a != 0 else 0)
    if x == '`':
        stack.append(1 if b>a else 0)
    return stack

def append_grid(grid, code):
    for rows in range(25):
        row = []
        for cols in range(80):
            row.append([])
        grid.append(row)
    code = code.split('\n')
    r = 0
    for line in code:
        c = 0
        for i in line:
            grid[r][c].append(i)
            c += 1
        r += 1
    return grid

print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
