class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        
        ans = 1
        for i in range(1, mn + 1):
            if mn % i == 0 and mx % i == 0:
                ans = i
        
        return ans
        
