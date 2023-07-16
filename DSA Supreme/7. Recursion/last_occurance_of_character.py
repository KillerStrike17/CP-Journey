mystr = "abcddeg"
x = "d"
# give me last occurance of character wit recursion

def find(str, index, target):
    print(str[index],index)
    if index <0:
        return -1
    if str[index] == target:
        return index
    return find(str, index-1, target)

print(find(mystr, len(mystr)-1, x))

