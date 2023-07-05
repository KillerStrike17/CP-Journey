mystr = "noavon"

mystr = list(mystr)
j = len(mystr)-1
for _ in range(0,len(mystr)//2):
    if mystr[_] == mystr[j]:
        j-=1
    else:
        print("Error")
        break
print("palindrome")