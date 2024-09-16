class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        temp = len(nums) - 1

        res = [0]*len(nums)

        for _ in reversed(range(len(nums))):
            if abs(nums[r] >= abs(nums[l])):
                val = nums[r]
                r -= 1
            
            else:
                val = nums[l]
                l += 1
            
            res[temp] = val**2
            temp -= 1
        return res







