class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        curr_sum = max_sum

        r = k
        while r < len(nums):
            curr_sum += nums[r] - nums[r-k]
            max_sum = max(max_sum, curr_sum)

            r += 1

        # for i in range(k, len(nums)):
        #     curr_sum += nums[i] - nums[i-k]
        #     max_sum = max(max_sum, curr_sum)

        return max_sum/k
