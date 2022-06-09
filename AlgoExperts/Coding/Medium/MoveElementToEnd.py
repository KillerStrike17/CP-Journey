def moveElementToEnd(array, toMove):
    # Write your code here.
    count = array.count(toMove)
    if count == 0:
        return array
    else:
        x = [_ for _ in array if _ != toMove]
        print(x)
        for _ in range(count):
            x.append(toMove)
        return x
