class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ratings = []

        for resto in restaurants:
            if resto[3] <= maxPrice and resto[4] <= maxDistance:
                if veganFriendly == 0 or resto[2] == veganFriendly:
                    ratings.append((resto[1], resto[0]))
        
        ratings.sort()

        ans = []

        for rate, id in ratings:
            ans.append(id)
        
        return ans[::-1]
