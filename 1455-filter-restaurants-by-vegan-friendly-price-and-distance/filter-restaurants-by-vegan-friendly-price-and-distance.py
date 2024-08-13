class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        ratings = []

        for resto in restaurants:
            if resto[3] <=maxPrice and resto[4] <= maxDistance:
                if veganFriendly == 0 or veganFriendly == resto[2]:
                    ratings.append((resto[1], resto[0]))
        

        res = []
        ratings.sort()

        for rate, id in ratings:
            res.append(id)
        
        return res[::-1]