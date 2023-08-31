class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price > buy:
                profit = max(profit, price - buy)
            else:
                buy = price
        
        return profit
    
    
    # def maxProfit(self, prices: list[int]) -> int:
    #     if not prices:
    #         return 0
        
    #     min_price = prices[0]
    #     max_profit = 0
        
    #     for price in prices:
    #         min_price = min(min_price, price)
    #         max_profit = max(max_profit, price - min_price)
        
    #     return max_profit
        