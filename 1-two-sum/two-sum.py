class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #leftIdx, rightIdx
        #leftVal = 2, 
        # [7,11,15]

        # [2,7,11,15]

        for i in range(len(nums) - 1):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i, j]
        
        