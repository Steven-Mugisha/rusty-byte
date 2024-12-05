class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in look_up:
                return [i, look_up[comp]]
            look_up[nums[i]] = i
        