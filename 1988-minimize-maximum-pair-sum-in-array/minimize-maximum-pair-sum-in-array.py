class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        temp = []
        size = len(nums)

        l, r  = 0, size - 1

        while l < r:
            temp.append(nums[l] + nums[r])
            l += 1
            r -= 1
        
        return max(temp)



