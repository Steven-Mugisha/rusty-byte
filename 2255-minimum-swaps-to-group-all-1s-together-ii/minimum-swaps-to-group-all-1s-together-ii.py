class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(nums)
        nums += nums
        zeros = width - sum(nums[:width])
        swaps = zeros
        for i in range(width, len(nums)):
            zeros += (nums[i] == 0)
            zeros -= (nums[i-width] == 0)
            swaps = min(swaps, zeros)
        
        return swaps
