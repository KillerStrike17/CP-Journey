myList= [1,2,3,4,5,6,7]
start = 0
end = len(myList) - 1
mid = (start + end)//2
target = 7
check = 0
while start<=end:
    if myList[mid] == target:
        check = 1
        # print("Found")
        break
    elif myList[mid]>target:
        end = mid - 1
    elif myList[mid]<target:
        start = mid+1
    mid = (start + end)//2

if check ==1:
    print("Found")
else:
    print("Not Found")