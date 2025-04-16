class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        look_up = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in look_up:
                look_up.remove(s[l])
                l += 1
            
            look_up.add(s[r])
            ans = max(ans, r - l + 1)
        
        return ans