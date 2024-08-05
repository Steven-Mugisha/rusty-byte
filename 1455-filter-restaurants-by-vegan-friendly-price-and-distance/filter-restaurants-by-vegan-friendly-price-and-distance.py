class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ratings, result = [], []

        for r in restaurants:
            if r[3] <= maxPrice and r[4] <= maxDistance:
                if veganFriendly == 0 or veganFriendly == r[2]:
                    ratings.append((r[1], r[0]))
        
        ratings.sort()

        for rate, id in ratings:
            result.append(id)
        
        return result[::-1]
        

