class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currMaxValue = sum(nums[:k])
        maxValue = currMaxValue

        for i in range(k, len(nums)):
            currMaxValue += nums[i] - nums[i-k]
            maxValue = max(maxValue, currMaxValue)
        
        return maxValue / k