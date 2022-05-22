# cook your dish here
from collections import Counter 
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    A_dict = Counter(A)
    # print(A_dict.items())
    # print(A)
    val = -1
    check_1 = check_2 = 0
    already = []
    for _ in A:
        if A_dict[_]>3 and check_1==0:
            val = _*_
            break
        elif A_dict[_]>1:
            # print(_)
            if check_1 ==0 :
                check_1=1
                val_1 = _
                already.append(_)
            if _ not in already and check_2 ==0:
                check_2 = 1
                val_2 = _
                break

    if check_1==1 and check_2==1:
        val = val_1*val_2
        