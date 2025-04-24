class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            
            # left sorted part:
            if nums[l] <= nums[mid]:
                if target in range(nums[l], nums[mid]):
                    r = mid - 1
                
                else:
                    l = mid + 1

            # right sorted part:
            else:
                if target in range(nums[mid], nums[r]+1):
                    l = mid + 1
                
                else:
                    r = mid - 1
        
        return -1 
