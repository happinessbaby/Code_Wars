
def find_outlier(integers):
        #check if one of the first two number is an outlier
        if integers[0] % 2 != integers[1] % 2:
            if integers[2] % 2 != integers[0] % 2:
                return integers[0]
            else:
                return integers[1]
        #find the outliers
        s = integers[1]
        for i in range(2, len(integers)):
            if (s + integers[i]) % 2 != 0:
                return integers[i]
            s = integers[i]

print(find_outlier([1, 2, 4, -2, -100]))
