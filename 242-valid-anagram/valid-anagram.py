class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1
        
        for ch in t:
            if ch not in counter:
                return False
            elif ch in counter:
                counter[ch] -= 1
                if counter[ch] == 0:
                    del counter[ch]
        
        return True
                