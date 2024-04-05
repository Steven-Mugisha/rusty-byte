class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0

        for sell in range(len(prices)):
            buy = min(buy, prices[sell])
            profit = max(profit, prices[sell] - buy)

        return profit