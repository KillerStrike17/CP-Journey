def flood(i, j, image, oldColor, newColor, n, m):
    if i < 0 or j < 0 or i == n or j == m or image[i][j] != oldColor:
        return
    image[i][j] = newColor
    flood(i+1, j, image, oldColor, newColor, n, m)
    flood(i-1, j, image, oldColor, newColor, n, m)
    flood(i, j+1, image, oldColor, newColor, n, m)
    flood(i, j-1, image, oldColor, newColor, n, m)


def floodFill(image, x, y, newColor):

    oldColor = image[x][y]
    if oldColor == newColor:
        return image
#     print(type(image))
    n = len(image)
    m = len(image[0])
    flood(x, y, image, oldColor, newColor, n, m)
    return image
    # Write your Code here.
