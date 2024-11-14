class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        product = [1]*n 

        for i in range(1, n):
            product[i] = nums[i-1] * product[i-1]
            
        prev_prod = nums[-1]

        for j in reversed(range(n-1)):
            product[j] *= prev_prod
            prev_prod *= nums[j]

        return product 