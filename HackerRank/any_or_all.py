N = int(input())
A = list(map(int, input().split()))
print(all([all([True if _ > 0 else False for _ in A]),
           any([True for _ in A if str(_) == str(_)[::-1]])]))
