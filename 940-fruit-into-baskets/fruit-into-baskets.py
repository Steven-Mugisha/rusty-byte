class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr_ans, ans = 0 , 0
        l = 0
        counter = defaultdict(int)

        for fr in range(len(fruits)):
            counter[fruits[fr]] += 1
            curr_ans += 1
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                curr_ans -= 1

                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
            ans = max(ans, curr_ans)
        
        return ans 
