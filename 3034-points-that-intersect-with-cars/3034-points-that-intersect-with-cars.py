class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        Mapset = set()
        
        for i in nums:
            for j in range(i[0], i[1] + 1):
                Mapset.add(j)
            
        return len(Mapset)




        
        

        