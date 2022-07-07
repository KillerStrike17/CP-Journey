my_arr = {}

def helper(index, temp_arr,temp_sum, n, denoms):
    if index == len(denoms):
        return 
    
    if temp_sum>n:
        return 
    
    if temp_sum ==n:
        x = tuple(temp_arr)
        if x not in my_arr:
            my_arr[tuple(x)] = 1
        return

    temp_sum += denoms[index]
    temp_arr.append(denoms[index])
    helper(index, temp_arr,temp_sum, n, denoms)
    temp_sum -= denoms[index]
    temp_arr.pop()

    helper(index+1, temp_arr,temp_sum, n, denoms)


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    global my_arr
    my_arr = {}
    helper(0, [],0, n, denoms)
    keys = list(my_arr.keys())
    keys.sort(key = len)
    print(keys)
    print(my_arr)
    if keys:
        return len(keys[0])
    return -1
            
            
    
    # pass
