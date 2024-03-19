class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(nums)
        nums += nums
        zeros = width - sum(nums[:width])
        ans = math.inf

        for r in range(width, len(nums)):
            zeros += nums[r- width]
            zeros -= nums[r]
            ans = min(ans, zeros)
        
        return ans