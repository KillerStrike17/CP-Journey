class Solution:
    def maxProfit(self, prices) -> int:
        buy_price = 1e10
        sell_price = 0
        len_prices = len(prices)
        profit = 0
        prev = prices[0]
        for _ in range(1,len_prices):
            
            if prev<prices[_]:
                profit += prices[_]-prev
                
            prev = prices[_]
        return profit