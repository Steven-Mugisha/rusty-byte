class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        currCount, res = 0, 0
        l = 0
        counter = defaultdict(int)

        for r in range(len(fruits)):
            currCount += 1
            counter[fruits[r]] += 1

            while len(counter) > 2:
                currCount -= 1
                counter[fruits[l]] -= 1

                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                
                l += 1
            
            res = max(res, currCount)
        
        return res