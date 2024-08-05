class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        rating = []
        res = []

        for resto in restaurants:
            if (resto[3] <= maxPrice) and (resto[4]<=maxDistance):
                if veganFriendly == 0 or veganFriendly == resto[2]:
                    rating.append([resto[1], resto[0]])    

        rating.sort()

        for i in rating:
            res.append(i[1])
        res.reverse()

        return res