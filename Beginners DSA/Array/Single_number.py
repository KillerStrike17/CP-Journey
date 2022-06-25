def occursOnce(a, n):
    a.sort()
    for _ in range(0, n, 2):
        if _ == n-1:
            return a[_]
        elif a[_] != a[_+1]:
            return a[_]
    # Write your code here.
    pass
