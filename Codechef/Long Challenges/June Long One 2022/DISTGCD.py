# cook your dish here
from functools import reduce

for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    X = abs(A-B)
    print(len(set(reduce(list.__add__,
                         ([i, X//i] for i in range(1, int(X**0.5)+1) if X % i == 0)))))
