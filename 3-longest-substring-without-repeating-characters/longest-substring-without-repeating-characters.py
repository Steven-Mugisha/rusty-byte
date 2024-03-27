class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        ans = 0
        curr_len = 0
        l = 0

        for r in range(len(s)):
            curr_len += 1
            while s[r] in count:
                count.remove(s[l])
                curr_len -= 1
                l += 1

            count.add(s[r])
            ans = max(ans, len(count))
        
        return ans
