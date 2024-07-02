class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     diff = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == diff:
        #             return [i, j]


        # TC: O(n*log(n)), SC: O(n)
        # map: {2: 0, 7: 1, ...}

        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]] = i
        


        
        