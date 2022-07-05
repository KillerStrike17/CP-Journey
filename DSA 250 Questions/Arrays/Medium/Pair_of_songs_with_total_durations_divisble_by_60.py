class Solution:

    def numPairsDivisibleBy60(self, time) -> int:
    
        counter = 0
        temp =[0]*60
        for _ in time:
            print(counter)
            counter += temp[- _%60]
            temp[_%60]+=1
        return counter
    