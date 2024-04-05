class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_max = sum(nums[:k])
        ans = curr_max

        for i in range(k, len(nums)):
            curr_max += nums[i] - nums[i-k]
            ans = max(ans, curr_max)

        return ans/k



