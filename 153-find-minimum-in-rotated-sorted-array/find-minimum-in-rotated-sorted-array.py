class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        boundary = -1

        while left <= right:
            mid = (left + right)// 2

            if nums[mid] <= nums[-1]:
                boundary = nums[mid]
                right = mid - 1
            
            else:
                left = mid + 1
        
        return boundary