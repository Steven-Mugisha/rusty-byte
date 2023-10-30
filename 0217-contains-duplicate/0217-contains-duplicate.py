class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        Mapset = set()
        
        for i in nums:
            if i in Mapset:
                return True
            Mapset.add(i)
        
        return False


    
 

        