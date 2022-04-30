for _ in range(int(input())):
    N = input()
    my_dict = {'0':6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
    count=0
    for _ in N:
        count += my_dict[_]
    if count%2==0:
        print((count//2) * '1')
    else:
        print("7"+(count-3)//2*'1')