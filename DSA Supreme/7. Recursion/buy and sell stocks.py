class Solution:

    def profit(self, prices, index, minPrice, maxProfit):
        if index == len(prices):
            return maxProfit
        
        if prices[index]<minPrice:
            minPrice = prices[index]
        todayProfit = prices[index] - minPrice
        if todayProfit>maxProfit:
            maxProfit = todayProfit
        # print(prices[index],minPrice, maxProfit,todayProfit)
        return self.profit( prices, index+1, minPrice, maxProfit)


    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = -100000000
        minPrice = 100000000
        return self.profit(prices, 0, minPrice, maxProfit)
        # return maxProfit