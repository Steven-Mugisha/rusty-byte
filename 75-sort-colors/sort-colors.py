class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right, current = 0, len(nums) - 1, 0

        for _ in range(len(nums)):
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            
            elif nums[current] == 1:
                current += 1
            
            else:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            

            
            
        



