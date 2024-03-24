class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0

        for c in range(len(s)-2):
            if s[c] != s[c+1] and s[c] != s[c+2] and s[c+1] != s[c+2]:
                print(s[c], s[c+1], s[c+2])
                ans += 1
    
        return ans
            
