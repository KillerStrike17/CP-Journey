# cook your dish here
for _ in range(int(input())):
    S,A,B,C = list(map(int, input().split()))
    final = S + S*C/100
    if final>=A and final<=B:
        print("Yes")
    else:
        print("No")