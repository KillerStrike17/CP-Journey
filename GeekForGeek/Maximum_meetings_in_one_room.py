from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        pair = [(S[i],F[i]) for i in range(N)]
        sort_pair = sorted(pair, key = lambda x:x[1])
        output = [pair.index(sort_pair[0])+1]
        # print('Pair:',pair)
        # print("Sort_pair:",sort_pair)
        end = sort_pair[0][1]
        for _ in range(1,N):
            # print(sort_pair[_][0],end)
            if sort_pair[_][0]>end:
                end = sort_pair[_][1]
                output.append(pair.index(sort_pair[_])+1)
                # print("Output:",output)
        output.sort()
        return output
        # code here
        



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
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends