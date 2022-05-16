# cook your dish here
for _ in range(int(input())):
    N = int(input())
    f = list(map(int, input().split()))
    total=0
    max_value = 0
    distance = 1
    for _ in range(N):
        if f[0] ==0:
            break
        else:
            if _ ==0:
                total = f[0]
            else:
                total += f[_] -1
                distance +=1
                if total ==0:
                    break
    print(distance+total-1)