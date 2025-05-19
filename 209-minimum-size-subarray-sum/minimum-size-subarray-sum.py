class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        
        curr_sum = l = 0
        ans = float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1    
        return ans