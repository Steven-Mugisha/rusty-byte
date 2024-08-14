class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = []
        lookUp = {}

        for index, resto in enumerate(list1):
            lookUp[resto] = index
        
        minIndex = float('inf')

        for index, resto in enumerate(list2):
            if resto in lookUp:
                currIndexSum = index + lookUp[resto]
                if currIndexSum < minIndex:
                    minIndex = currIndexSum
                    common_strings = [resto]
                    
                elif currIndexSum == minIndex:
                    common_strings.append(resto)
                
        return common_strings



        