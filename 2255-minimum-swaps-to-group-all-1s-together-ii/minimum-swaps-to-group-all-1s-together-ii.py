class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        width = sum(nums)
        nums += nums
        currZeros = width - sum(nums[:width])
        res = currZeros

        for i in range(width, len(nums)):
            currZeros += (nums[i] == 0)
            currZeros -= (nums[i- width] == 0)

            res = min(res, currZeros)
        
        return res