class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map = {}

        for index, string in enumerate(list1):  # O(list1)
            map[string] = index

        min_index = float('inf')
        result = []

        for index, string in enumerate(list2): # O(list2) 
            if string in map:
                temp_index = index + map[string]
                if temp_index < min_index:
                    min_index = temp_index
                    result = [string]
                
                elif temp_index == min_index:
                    result.append(string)
        
        return result



