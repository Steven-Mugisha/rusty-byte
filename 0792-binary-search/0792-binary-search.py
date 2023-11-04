class Solution:
    def search(self, nums: List[int], target: int) -> int:

        R, L = 0, len(nums) - 1

        while R <= L:
            mid = (R + L) // 2
            res = nums[mid]

            if res == target:
                return mid
            
            if res > target:
                L = mid - 1
            
            else:
                R = mid + 1
        
        return -1 

        



        