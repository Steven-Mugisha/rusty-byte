class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        ans = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            ans = max(ans, curr_sum)

        return ans/k
