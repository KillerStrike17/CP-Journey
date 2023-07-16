class Solution:

    def mincostTicketHelper(self,days,costs,i):
        if i>=len(days):
            return 0
        
        cost1 = costs[0]+self.mincostTicketHelper(days, costs,i+1)

        passEndDay = days[i]+7-1
        j = i
        while(j<len(days) and days[j]<=passEndDay):
            j+=1
        
        cost7 = costs[1]+self.mincostTicketHelper(days, costs,j)

        passEndDay = days[i]+30-1
        j = i
        while(j<len(days) and days[j]<=passEndDay):
            j+=1
        
        cost30 = costs[2]+self.mincostTicketHelper(days, costs,j)

        return min(cost1, cost7, cost30)



    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.mincostTicketHelper(days,costs,0)