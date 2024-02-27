class Solution:
    def minimumSteps(self, s: str) -> int:
        j = 0
        c = 0
        for i in range(len(s)):
            if s[i] == '0':
                c += i - j
                j += 1
        return c


        
        