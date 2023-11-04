class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L+R) //2
            guess = nums[mid]

            if guess == target:
                return mid
            
            if guess > target:
                R = mid - 1
            
            else:
                L = mid + 1

        return L

        