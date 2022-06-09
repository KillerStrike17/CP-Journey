def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    min = 10**9
    pair = []
    for _ in arrayOne:
        for k in arrayTwo:
            if abs(k-_) < min:
                min = abs(k-_)
                pair = [_, k]
    return pair
    pass

# Or


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    id_One = id_Two = 0
    small = 10**9
    current = 10**9
    smallestPair = []
    while id_One < len(arrayOne) and id_Two < len(arrayTwo):
        first_num = arrayOne[id_One]
        second_num = arrayTwo[id_Two]
        if first_num > second_num:
            current = first_num - second_num
            id_Two += 1
        elif first_num < second_num:
            current = second_num - first_num
            id_One += 1
        else:
            return [first_num, second_num]
        if small > current:
            small = current
            smallestPair = [first_num, second_num]
    return smallestPair
