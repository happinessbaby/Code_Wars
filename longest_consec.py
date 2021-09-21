
def longest_consec(strarr, k):
    chunks = [strarr[i:i+k] for i in range(len(strarr)-k+1)]
    string = [''.join(chunks[i]) for i in range(len(chunks))]
    return max(string, key = len) if strarr and 0<k<=len(strarr) else ""

print(longest_consec(['ab', 'asd', 'sdf', '3w4g'], 3))
