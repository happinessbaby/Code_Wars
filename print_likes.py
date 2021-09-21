
def likes(list):
    if len(list) < 1:
        return "no one likes this"
    elif len(list) == 1:
        return f"{list[0]} likes this"
    elif len(list) == 2:
        return f"{list[0]} and {list[1]} like this"
    elif len(list) == 3:
        return f"{list[0]}, {list[1]}, and {list[2]} like this"
    else:
        n = len(list) - 2
        return f"{list[0]}, {list[1]}, and {n} others like this"


print(likes([])) # must be "no one likes this"
print(likes(["Peter"])) # must be "Peter likes this"
print(likes(["Jacob", "Alex"])) # must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"])) # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"])) # must be "Alex, Jacob and 2 others like this"
