class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,ans = 0, math.inf
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                ans = min(ans, r - l +1)
                curr_sum -= nums[l]
                l += 1
        return ans if ans != math.inf else 0

