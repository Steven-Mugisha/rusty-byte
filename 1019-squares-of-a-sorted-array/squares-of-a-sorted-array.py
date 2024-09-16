class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        # temp = len(nums) - 1

        res = [0]*len(nums)

        for i in reversed(range(len(nums))):
            if abs(nums[r] >= abs(nums[l])):
                val = nums[r]
                r -= 1
            
            else:
                val = nums[l]
                l += 1
            
            res[i] = val**2
        
        return res







