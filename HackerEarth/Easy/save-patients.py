N = input()                  # Reading input from STDIN
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) > sum(B):
    print("No")
else:
    print("Yes")
