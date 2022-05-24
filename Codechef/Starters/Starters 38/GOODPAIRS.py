# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    my_dict = {}
    counter_a = counter_b = 0
    for i in range(N):
        x = (A[i], B[i])
        if x in my_dict.keys():
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    for key, val in my_dict.items():
        l, r = key[0], key[1]
        if (r, l) in my_dict.keys():
            if l != r:
                counter_a += my_dict[(l, r)] * my_dict[(r, l)]
            else:
                counter_b += my_dict[(l, r)]*(my_dict[(l, r)]-1)//2
    print(counter_a//2 + counter_b)
