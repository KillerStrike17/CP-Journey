# cook your dish here
for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    if A % 3 == 0 or B % 3 == 0:
        print(0)
    elif abs(A-B) % 3 == 0:
        print(1)
    elif abs(A-B) % 3 == 1:
        print(2)
    elif abs(A-B) % 3 == 2:
        print(2)
