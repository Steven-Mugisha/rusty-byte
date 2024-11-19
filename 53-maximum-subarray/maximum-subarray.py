class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = global_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            
            else:
                curr_sum += nums[i]
            
            global_sum = max(global_sum, curr_sum)
        
        return global_sum