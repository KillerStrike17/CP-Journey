# cook your dish here
for _ in range(int(input())):
    N = int(input())
    my_str = str(N) + " 1"
    last_val = N
    diff = abs(N-1)-1
    my_list = [1, N]
    while diff != 0:
        if diff >= last_val:
            x = diff + last_val
            if x > N:
                x = abs(last_val-diff)
                my_str = str(x) + " " + my_str
                last_val = x
            else:
                my_str = str(x) + " " + my_str
                last_val = x
        else:
            x = abs(last_val-diff)
            if x not in my_list:
                my_str = str(x) + " " + my_str
                last_val = x
            else:
                x = diff + last_val
                my_str = str(x) + " " + my_str
                last_val = x
        my_list.append(x)
        # print(my_list)

        diff -= 1
    print(my_str)
