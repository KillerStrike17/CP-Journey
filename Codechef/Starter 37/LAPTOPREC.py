# cook your dish here
from collections import Counter
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    mydict = Counter(A)
    sorted_dict = {k:v for k,v in sorted(mydict.items(), key = lambda item:item[1])}
    # sorted_dict = dict(sorted(mydict.sorted()))
    
    # print(mydict)
    my_list = list(sorted_dict.values())
    my_keys = list(sorted_dict.keys())
    # print(my_list)
    if len(my_list)>1:
        if my_list[-1] ==my_list[-2]:
            print("CONFUSED")
        else:
            print(my_keys[-1])
    else:
        print(my_keys[-1])