class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        temp = []

        for resto in restaurants:
            if resto[3] <= maxPrice and resto[4] <= maxDistance:
                if resto[2] == veganFriendly or veganFriendly == 0:
                    temp.append([resto[1], resto[0]])
        
        
        
        temp = sorted(temp)
        
        ans = [id for _, id in temp]

        return ans[::-1]



