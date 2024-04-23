class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i + 1)
        return ans