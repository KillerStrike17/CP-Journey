# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    odd_A = [x for x in A if x&1]
    even_A = [x for x in A if x%2==0]
    odd_len = len(odd_A)
    even_len =len(even_A) 
    if odd_len==0 or even_len==0:
        print("0")
    else:
        if odd_len%2==0:
            if odd_len//2 >even_len:
                print(even_len)
            else:
                print(odd_len//2)
        else:
            print(even_len)