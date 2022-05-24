# cook your dish here
for _ in range(int(input())):
    N, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    counter = 0
    my_dict = {}
    for i in range(N):
        if A[i] in my_dict:
            my_dict[A[i]] += 1
        else:
            my_dict[A[i]] = 1
    # print(my_dict)
    for i in range(N):

        val = (k-A[i]) ^ A[i]
        # print(val,A[i])
        if val in my_dict:
            counter += my_dict[val]
            if A[i] == val:
                counter -= 1
        my_dict[A[i]] -= 1
    print(counter)
