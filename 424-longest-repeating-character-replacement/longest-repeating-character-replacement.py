class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        curr_max = 0
        result = 0

        for r in range(len(s)):
            curr_max += 1
            counter[s[r]] += 1

            while (curr_max - max(counter.values())) > k:
                counter[s[l]] -= 1
                curr_max -= 1
                l += 1
            
            result = max(result, curr_max)
        
        return result