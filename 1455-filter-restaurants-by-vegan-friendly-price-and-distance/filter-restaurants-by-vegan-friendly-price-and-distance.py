class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ratings = []
        for r in restaurants:
            if r[3] <= maxPrice and r[4] <= maxDistance:
                if veganFriendly == 0 or r[2] == veganFriendly:
                    ratings.append([r[1], r[0]])
        
        ratings.sort()

        res = []

        for rate, id in ratings:
            res.append(id)
        
        return res[::-1]
                    

                    
