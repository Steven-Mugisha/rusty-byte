class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,l = 0,0
        counter = set()

        for r in range(len(s)):
            while s[r] in counter:
                counter.remove(s[l])
                l += 1
            
            counter.add(s[r])
            res = max(res, len(counter))
        
        return res
