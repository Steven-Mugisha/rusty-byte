class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        for c in s:
            if len(stack1) != 0 and c == '#':
                stack1.pop()
            elif c != '#':
                stack1.append(c)
        
        for c in t:
            if len(stack2) != 0 and c == '#':
                stack2.pop()
            
            elif c != '#':
                stack2.append(c)
        
        if stack1 == stack2:
            return 1
        
        else:
            return 0
            
     
            