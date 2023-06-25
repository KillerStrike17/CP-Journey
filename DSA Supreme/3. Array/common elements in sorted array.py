A = [1,5,10,20,40,80]
B = [6,7,20,80,100]
C = [3,4,15,20,30,70,80,120]
nA = len(A)
nB = len(B)
nC = len(C)
i = j = k = 0

while (i<nA and j<nB and k<nC):
    if (A[i] == B[j]) and (B[j] == C[k]):
        print(A[i])
        i +=1
        j +=1
        k +=1
    elif (A[i]<B[j]):
        i+=1
    elif (B[j]<C[k]):
        j+=1
    else:
        k+=1
    

