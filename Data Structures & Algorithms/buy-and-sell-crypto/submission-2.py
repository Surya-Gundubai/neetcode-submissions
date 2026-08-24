class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0
        for i in range(length):
            for j in range(i+1,length):
                if prices[i] < prices[j]:
                    profit_diff = prices[j] - prices[i]
                    max_profit = max(max_profit, profit_diff)
        return max_profit
                

        