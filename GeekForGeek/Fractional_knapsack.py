#User function Template for python3
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        # print(W)
        # print(Items)
        per_unit = [(i.value/i.weight,i.value, i.weight) for i in Items]
        # print(per_unit)
        sort_unit = sorted(per_unit, key = lambda x:x[0], reverse= True)
        # print(sort_unit)
        total =0
        for _ in sort_unit:
            # print(W,total)
            if W ==0: 
                break
            if _[2]>W:
                # print("Difference:",_[2]-W)
                total+=(W)*_[0]
                break
            else:
                total+=_[1]
                W -= _[2]
                
        return total
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends