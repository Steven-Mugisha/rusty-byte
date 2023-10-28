class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        windowSet = set()

        l = 0

        for r in range(len(nums)):

            if r - l > k:
                windowSet.remove(nums[l])
                l += 1

            if nums[r] in windowSet:
                return True
            
            windowSet.add(nums[r])

