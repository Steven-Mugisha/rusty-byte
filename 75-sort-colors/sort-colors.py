class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        curr, l, r = 0,0, len(nums) - 1

        for _ in range(len(nums)):
            if nums[curr] == 0:
                nums[curr], nums[l] = nums[l], nums[curr]
                curr += 1
                l += 1
            
            elif nums[curr] == 1:
                curr += 1
            
            else:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
        
        return nums