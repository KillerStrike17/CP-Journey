A = [9,5,4,9]
B = [2,1,4]
nA = len(A)-1
nB = len(B)-1
C = 0
output = []

while(nA>=0 and nB>=0):
    x = A[nA] + B[nB] + C
    digit = x%10
    
    C = C//10
    
    
