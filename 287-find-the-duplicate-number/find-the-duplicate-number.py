class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     if nums[index] < 0:
        #         return abs(nums[i])
        #     nums[index] = -nums[index]

        for n in range(len(nums)):
            get_index = abs(nums[n]) - 1
            if nums[get_index] < 0:
                return abs(nums[n])
            nums[get_index] = -nums[get_index]
    