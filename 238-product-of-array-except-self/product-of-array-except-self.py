class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,3,4]

        # pre = [1,1,2,6]
        # suff = [24, 12, 4,1] # 

        # ans = [24, 12,8,6]

        prefix = [1]
        prod = 1

        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            prefix.append(prod)
        
        suffix = [0] * len(nums)
        prod2 = 1
        suffix[len(nums) - 1] = prod2

        for j in range(len(nums) - 2, -1, -1):
            prod2 *= nums[j + 1]
            suffix[j] = prod2

        result = []
        for x in range(len(prefix)):
            result.append(prefix[x] * suffix[x])
        
        return result

        

        



        



