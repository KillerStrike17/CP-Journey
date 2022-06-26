from typing import List


def countNegativeNumbers(mat: List[List[int]]) -> int:
    # write nyour code here
    x= [j for i in mat for j in i if j<0]
#     print(x)
    return len(x)
    pass
