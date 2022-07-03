class Solution:
    def maxProfit(self, prices) -> int:
        val = 0
        buy_price = 1e10
        sell_price = 0
        len_price = len(prices)
        for _ in range(len_price):
            # print(buy_price, sell_price)
            buy_price = min(buy_price,prices[_])
            sell_price = max(sell_price, prices[_]-buy_price)
            
        return sell_price