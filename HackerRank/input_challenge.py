# Enter your code here. Read input from STDIN. Print output to STDOUT
A, B = list(map(int, input().split()))
pol = input()
if B == eval(pol.replace('x', str(A))):
    print("True")
else:
    print("False")
