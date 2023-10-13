class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        new_set = set()
        
        for i in nums:
            new_set.add(i)
        
        return True if len(nums) != len(new_set) else False


        