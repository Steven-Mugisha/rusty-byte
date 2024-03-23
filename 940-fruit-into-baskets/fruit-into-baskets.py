class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,ans, total = 0,0,0
        counter = defaultdict(int)

        for r in range(len(fruits)):
            counter[fruits[r]] += 1
            total += 1

            while len(counter) > 2:
                f = fruits[l]
                counter[f] -= 1
                total -= 1

                if counter[f] == 0:
                    del counter[f]
                    
                l += 1

            ans = max(ans, total)
        return ans
        