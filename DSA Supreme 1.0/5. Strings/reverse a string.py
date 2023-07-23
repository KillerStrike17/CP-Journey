name = "Shubham"
print(name)
print(name[::-1])

i = 0
j = len(name)-1
name = list(name)
for _ in range(0,len(name)//2):
    name[i],name[j] = name[j],name[i]
    i+=1
    j-=1
print("".join(name))