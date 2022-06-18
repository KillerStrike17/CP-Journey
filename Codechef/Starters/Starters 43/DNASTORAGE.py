# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = input()
    mystr = ""
    for _ in range(0, N, 2):
        if S[_]+S[_+1] == "00":
            mystr += 'A'
        elif S[_]+S[_+1] == "01":
            mystr += 'T'
        elif S[_]+S[_+1] == "10":
            mystr += 'C'
        elif S[_]+S[_+1] == "11":
            mystr += 'G'
    print(mystr)
