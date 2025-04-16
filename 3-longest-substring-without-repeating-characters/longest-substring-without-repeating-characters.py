class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        look_up = set()
        ans = 0
        left = 0

        for right in range(len(s)):
            while s[right] in look_up:
                look_up.remove(s[left])
                left += 1
            look_up.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans

