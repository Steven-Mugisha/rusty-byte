class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            c = 1
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                c += 1
                r += 1
            for _ in range(min(2, c)):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l

        
      
     