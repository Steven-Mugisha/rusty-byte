class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0, 1
        Profit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                cur_profit = prices[j] - prices[i]
                Profit = max(Profit, cur_profit)
            
            else:
                i = j
            j += 1
        return Profit


