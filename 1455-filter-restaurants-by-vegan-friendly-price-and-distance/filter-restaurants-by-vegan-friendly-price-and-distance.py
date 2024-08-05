class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        rating = []
        res = []

        for r in restaurants:
            if r[3] <= maxPrice and r[4] <= maxDistance:
                if veganFriendly == 0 or veganFriendly == r[2]:
                    rating.append([r[1], r[0]])
        
        rating.sort()

        print(f'rating here {rating}')

        for i in rating:
            res.append(i[1])
        
        print(f'res {res}')
        
        return res[::-1]


