from typing import List

class Solution:
    def beautifulArray(self,arr : List[int], x : int, k : int) -> int:
        # code here
        arr.sort()
        print(arr)
        temp =[]
        for i in range(1,len(arr)):
            if (arr[i] - arr[i-1])>k:
                temp.append(arr[i] - arr[i-1])
        temp.sort()
        counter =0
        print(temp)
        for i in range(len(temp)):
            val = temp[i]
            print("Val:",val)
            diff = val // k
            print("Diff:",diff)
            if val % k == 0:
                diff -= 1
            mini = min(x,diff)
            print("Mini:",mini)
            x -= mini
            print("X:",x)
            val -= mini*k
            print("Val:",val)
            print("Counter:",counter)
            if val <= k:
                counter += 1
                print("updated counter:",counter)
            if x < 0:
                break
        
        final_result = len(temp) - counter + 1
        print("Final result:",final_result)
        return final_result

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    # t = int(input())
    t = 1
    for _ in range(t):
        
        # n = int(input())
        
        n = 10
        # arr=IntArray().Input(n)
        arr = [1,1,3,1,1,5,1,1,7,9]
        
        
        # x,k = map(int,input().split())
        x,k = 3,1
        
        
        obj = Solution()
        res = obj.beautifulArray( arr, x, k)
        
        print(res)
        

# } Driver Code Ends