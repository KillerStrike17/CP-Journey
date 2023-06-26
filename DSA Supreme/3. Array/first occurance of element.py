myList= [4,5,6,7]
def bs():

    start = 0
    end = len(myList) - 1
    mid = (start + end)//2
    target = 3
    check = 0
    index = -1
    while start<=end:
        if myList[mid] == target:
            index = mid
            end = mid-1
            # print("Found")
            # break
        elif myList[mid]>target:
            end = mid - 1
        elif myList[mid]<target:
            start = mid+1
        mid = (start + end)//2

    # if check ==1:
    #     print("Found")
    # else:
    #     print("Not Found")
    print(index)

bs()