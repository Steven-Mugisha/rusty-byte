class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        ans,l = 0,0
        
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1
            Set.add(s[r])
            ans = max(ans, len(Set))
        
        return ans