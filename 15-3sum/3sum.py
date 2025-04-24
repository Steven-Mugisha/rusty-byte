class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, val in enumerate(nums):
            if index > 0 and val == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums)-1
            while left < right:
                _3sum = val + nums[left] + nums[right]

                if _3sum < 0:
                    left += 1
                
                elif _3sum > 0:
                    right -= 1
                
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res