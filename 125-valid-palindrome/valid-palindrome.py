class Solution:


    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        t = [x for x in s if x.isalnum()]

        i,j = 0, len(t)-1

        while i < j:
            if t[i] != t[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True




