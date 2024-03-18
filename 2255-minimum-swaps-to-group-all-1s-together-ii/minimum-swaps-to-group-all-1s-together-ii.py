class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        nums += nums
        zeros = ones - sum(nums[:ones])
        n_swaps = zeros
        
        for i in range(ones, len(nums)):
            zeros += nums[i - ones]
            zeros -= nums[i]
            n_swaps = min(n_swaps, zeros)
        
        return n_swaps

