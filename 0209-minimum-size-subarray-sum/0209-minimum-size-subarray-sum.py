class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, currSum = 0, 0
        minLength = float("inf") 
    
        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                minLength = min(minLength, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        return 0 if minLength == float("inf") else minLength


        