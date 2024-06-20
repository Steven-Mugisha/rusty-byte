class Solution:
    def findGCD(self, nums: List[int]) -> int:

        min_val, max_val = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            
            if nums[i] < min_val:
                min_val = nums[i]
    
        return gcd(min_val, max_val)
    
            
