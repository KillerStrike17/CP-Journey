mylist = [1,2,3,4,4,4,4,4,4,5]
target = 4

def lowerbound(mylist:list, target:int)->int:
    start = 0
    end = len(mylist)-1
    mid = start + (end-start)//2
    index = -1
    while start<=end:
        if mylist[mid]==target:
            end = mid -1
            index = mid
        elif mylist[mid]>target:
            end = mid -1
        else:
            start = mid +1
        mid = start + (end-start)//2
    return index

def upperbound(mylist:list, target:int)->int:
    start = 0
    end = len(mylist)-1
    mid = start + (end-start)//2
    index = -1
    while start<=end:
        if mylist[mid]==target:
            start = mid +1
            index = mid
        elif mylist[mid]>target:
            end = mid -1
        else:
            end = mid +1
        mid = start + (end-start)//2
    return index

print("Lower Bound:",lowerbound(mylist, target))
print("Upper Bound:",upperbound(mylist, target))
print("Total Occurance:",upperbound(mylist, target)-lowerbound(mylist, target) + 1)