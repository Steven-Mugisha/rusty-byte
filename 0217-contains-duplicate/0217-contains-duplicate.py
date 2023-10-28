class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        MapSet = set()
        
        for i in nums:

            if i in MapSet:
                return True

            MapSet.add(i)
        
        return False 

        

 

        