# cook your dish here
for _ in range(int(input())):
    A,B = list(map(int, input().split()))
    first_val = A*10
    second_val = B*5
    if first_val==second_val:
        print("ANY")
    elif first_val>second_val:
        print("FIRST")
    else:
        print("SECOND")