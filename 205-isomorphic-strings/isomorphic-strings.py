class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        lookUp, reverse = {}, {}
        for i in range(len(s)):
            if (s[i] in lookUp and lookUp[s[i]] != t[i]) or (t[i] in reverse and reverse[t[i]] != s[i]):
                return False        
            else:
                reverse[t[i]] = s[i]
                lookUp[s[i]] = t[i]
        
        return True
