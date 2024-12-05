class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}

        for i, num in enumerate(nums):
            look_up[num] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in look_up and look_up[comp] != i:
                return [i, look_up[comp]]
        