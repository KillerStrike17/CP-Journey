arr = [12,16,22,30,35,39,42,45,48,50,53,55,56]
low = 0
high = len(arr)-1
k = 4
x = 35
while high-low>k:
    if (x - arr[low])>(arr[high]-x):
        low+=1
    else:
        high-=1
print(arr[low:high])


