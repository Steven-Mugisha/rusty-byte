class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:      
        map = {}
        minVal = float('inf')
        res = []

        for idx, string in enumerate(list1):
            map[string] = idx
        
        for idx, string in enumerate(list2):
            if string in map:
                totalIdx = idx + map[string]

                if totalIdx < minVal:
                    minVal = totalIdx
                    res = [string]
                
                elif totalIdx == minVal:
                    res.append(string)
        
        return res