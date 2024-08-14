class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s)-1, len(t)-1

        while p1 >= 0 or p2 >= 0:
            backspace_count = 0

            while p1 >= 0:
                if s[p1] == '#':
                    backspace_count += 1
                    p1 -= 1
                
                elif backspace_count > 0:
                    backspace_count -= 1
                    p1 -= 1
                
                else:
                    break
            
            backspace_count = 0
            while p2 >= 0:
                if t[p2] == '#':
                    backspace_count += 1
                    p2 -= 1
                
                elif backspace_count > 0:
                    backspace_count -= 1
                    p2 -= 1
                
                else:
                    break
            
            if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                return False
            
            if (p1 >=0) != (p2 >=0):
                return False
            
            p1 -= 1
            p2 -= 1
            
        
        return True
        
     
            