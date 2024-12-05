class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = set()
        ans = 0
        l = 0

        for r in range(len(s)):
            
            while s[r] in counter:
                counter.remove(s[l])
                l += 1
            counter.add(s[r])
            ans = max(ans, r - l + 1)

        
        return ans

                    

                


