class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        prefix = 1
        sufix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            result.append(prefix)

        for j in range(len(nums) - 2, -1, -1):
            sufix *= nums[j + 1]
            result[j] *= sufix
        
        return result

        

        



        



