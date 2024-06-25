class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = 0

        for i in range(n):
            temp = nums[i]
            while (temp < n and nums[temp] != temp):
                nums[temp], temp = temp, nums[temp]
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n