class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res, l = 0, 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        
        return res
            