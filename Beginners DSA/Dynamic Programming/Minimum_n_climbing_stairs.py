class Solution:
    my_dict = {}
    def solve(self, cost, n):
        global my_dict 
        
        if n==0 or n==1:
            return cost[n]
        if n in my_dict:
            return my_dict[n]
        ans = cost[n] + min(self.solve(cost,n-1),self.solve(cost,n-2))
        my_dict[n] = ans
        return  my_dict[n]
            

    def solve2(self, cost, n):
        global my_dict
        my_dict[0] = cost[0]
        my_dict[1] = cost[1]
        for _ in range(2, n+1):
            my_dict[_]=cost[_]+min(my_dict[_-1],my_dict[_-2])
        return my_dict[n]

    def solve3(self, cost, n):
        prev_1 = cost[1]
        prev_2= cost[0]
        # curr = cost[0]+min(prev_1,prev_2)
        for _ in range(2, n):
            curr=cost[_]+min(prev_1,prev_2)
            prev_2 = prev_1
            prev_1 = curr
            
        return min(prev_1, prev_2)                    
            
    
    def minCostClimbingStairs(self, cost) -> int:
        global my_dict
        my_dict = {}
        n = len(cost)
        # ans = min(self.solve(cost, n-1),self.solve(cost,n-2))
        ans = self.solve3(cost, n)
        return ans
        
        