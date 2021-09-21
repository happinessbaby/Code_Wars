import functools

memo = {}
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    for col in range(len(matrix)):
        m = [row[:col]+row[col+1:] for row in matrix[1:]]
        memo[str(n)+':'+str(col)] = (-1)**col * matrix[0][col] * determinant(m)
    memo[n] = sum(memo[str(n)+':'+str(col)] for col in range(len(matrix)))
    return memo[n]

def determinant2(matrix):
    return functools.reduce(lambda m, col: m + (-1)**col * matrix[0][col] *
determinant([row[:col]+row[col+1:] for row in matrix[1:]]), range(len(matrix)), 0) if len(matrix) > 1 else matrix[0][0]

m2 = [[2,5,3, 4], [1,-2,-1, -3], [1, 3, 4, 5], [-2, -4, 10, 5]]
print(determinant(m2))
