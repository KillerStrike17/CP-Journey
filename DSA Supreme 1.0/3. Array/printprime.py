def checkprime(n:int)->bool:
    if n==1:
        return False
    for _ in range(2,n//2+1):
        if n %_ ==0:
            return False
    return True

def printprime(n:int):
    for _ in range(1,n+1):
        if checkprime(_):
            print(_)

printprime(100)