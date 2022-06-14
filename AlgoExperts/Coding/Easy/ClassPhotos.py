def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    x = True
    y = True
    for _ in range(len(redShirtHeights)):
        if _ == 0:
            if redShirtHeights[_] > blueShirtHeights[_]:
                check_1 = 1
            elif redShirtHeights[_] < blueShirtHeights[_]:
                check_1 = 2
            else:
                x = False
                y = False
                break
        elif check_1 == 1:
            if redShirtHeights[_] <= blueShirtHeights[_]:
                x = False
                y = False
                break
        elif check_1 == 2:
            if redShirtHeights[_] >= blueShirtHeights[_]:
                x = False
                y = False
                break
    return x and y
