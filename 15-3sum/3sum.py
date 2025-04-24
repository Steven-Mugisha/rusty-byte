class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i -1]:
                continue
            
            l, r = i + 1, len(nums)-1

            while l < r:
                threesum = val + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                
                elif threesum > 0:
                    r -= 1
                
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        return res

