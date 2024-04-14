class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, counter = 0, defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            maxCount = max(counter.values())
            while ((r - l + 1) - maxCount) > k:
                counter[s[l]] -= 1

                if counter[s[l]] == 0:
                    del counter[s[l]]

                l += 1
            
            res = max(res, r - l + 1)
        return res

                