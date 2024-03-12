class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float: 
        max_sum = sum(nums[:k])
        curr_sum = max_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)

        return max_sum/k



        
        # while r <= len(nums) - 1:
        #     curr_sum = maximum - nums[l] + nums[r]
        #     maximum = max(maximum, curr_sum)
        #     r += 1
        #     l += 1
        
        # aver = maximum/k

        # return aver

