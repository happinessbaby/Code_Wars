def strip_char(string, markers):
    i = 0
    while i < len(string):
        if string[i] in markers:
            s1 = string[:i].rstrip() #strip end of the line whitespace
            for j in range(len(string[i:])):
                if string[j] == '\n':
                    string = s1 + string[j:] #remove: string[i+1:j]
                    break
                if j == len(string[i:])-1:
                    string = s1.rstrip() #strip end of the line whitespace
                    i += len(string) #break out of the while loop and return answer
        else:
            i += 1
    return string.replace(' +', ' ') #strip extra whitespace in the middle

print(strip_char("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(strip_char("a #b\nc\nd $e f g", ["#", "$"]))
