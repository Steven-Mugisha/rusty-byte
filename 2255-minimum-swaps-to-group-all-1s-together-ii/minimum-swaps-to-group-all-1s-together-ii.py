class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(nums)
        nums += nums
        zeros = width - sum(nums[:width])
        no_swaps = zeros

        for i in range(width, len(nums)):
            zeros += (nums[i] == 0)
            zeros -= (nums[i - width] == 0)
            no_swaps = min(no_swaps, zeros)
        
        return no_swaps