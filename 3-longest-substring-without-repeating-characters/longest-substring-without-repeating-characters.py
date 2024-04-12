class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        currLength, res = 0, 0
        l = 0

        for r in range(len(s)):
            currLength += 1
            while s[r] in seen:
                currLength =- 1
                seen.remove(s[l])
                l += 1
                
            print("seen here: ", seen)
            seen.add(s[r])
            res = max(res, len(seen))
        
        return res
            