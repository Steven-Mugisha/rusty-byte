class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        windowSum = sum(nums[0:k])
        maxSum = windowSum

        for i in range(0, len(nums)-k):
            windowSum = windowSum + nums[i + k] - nums[i]
            maxSum = max(maxSum, windowSum)


        return maxSum/k
