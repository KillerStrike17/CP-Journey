my_array = []


def search(arr, n, temp_str, i, j):

    if i < 0 or j < 0 or i == n or j == n or arr[i][j] == 0:
        return
    elif i == n-1 and j == n-1:
        print(temp_str)
        my_array.append(temp_str)
        return
    else:
        arr[i][j] = 0
        temp_str += "D"
        search(arr, n, temp_str, i+1, j)
        temp_str = temp_str[:-1]
        temp_str += "L"
        search(arr, n, temp_str, i, j-1)
        temp_str = temp_str[:-1]
        temp_str += "R"
        search(arr, n, temp_str, i, j+1)
        temp_str = temp_str[:-1]
        temp_str += "U"
        search(arr, n, temp_str, i-1, j)
        temp_str = temp_str[:-1]
        arr[i][j] = 1


def searchMaze(arr, n):
    # Write your code here.
    global my_array
    my_array = []
    visited = [[0]*n]*n
    # print(visisted)
    search(arr, n, "", 0, 0)
    return my_array


x = [[1, 0],
     [1, 1]]
print(searchMaze(x, 2))
