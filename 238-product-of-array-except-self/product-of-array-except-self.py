class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        prod = 1
        prod2 = 1

        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            result.append(prod)
            
        for j in range(len(nums) - 2, -1, -1):
            prod2 *= nums[j + 1]
            result[j] *= prod2
        
        return result

        

        



        



