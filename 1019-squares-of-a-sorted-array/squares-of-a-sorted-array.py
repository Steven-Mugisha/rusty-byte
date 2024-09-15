class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        result = [0]*n

        for i in reversed(range(n)):
            if abs(nums[r]) >= abs(nums[l]):
                temp = nums[r]
                r -= 1
            
            else:
                temp = nums[l]
                l += 1
            
            result[i] = temp**2
        return result