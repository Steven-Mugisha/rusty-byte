class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l, res, currLength = 0, 0, 0

        for r in range(len(s)):
            currLength += 1
            counter[s[r]] += 1
            maxCount = max(counter.values())
            while (currLength - maxCount) > k:
                counter[s[l]] -= 1
                currLength -= 1
                l += 1
            
            res = max(res, currLength)
        
        return res
