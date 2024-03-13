class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(nums)
        nums += nums
        # res = width
        curr_zeros = len(nums[:width]) - sum(nums[:width])
        res = curr_zeros
        for i in range(width, len(nums)):
            curr_zeros -= (nums[i - width] == 0)
            curr_zeros += (nums[i] == 0)
            res = min(res, curr_zeros)
        
        return res
            

