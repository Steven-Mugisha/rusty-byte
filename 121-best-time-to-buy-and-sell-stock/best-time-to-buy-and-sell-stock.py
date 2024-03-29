class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], 0
        Profit = 0

        while sell < len(prices):
            buy = min(buy, prices[sell])
            Profit = max(Profit, prices[sell] - buy)
            sell += 1
        
        return Profit


        