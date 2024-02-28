class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        Stack = []

        for b in s:
            if b in brackets:
                Stack.append(b)
                
            elif len(Stack) == 0 or b != brackets[Stack.pop()]:
                return False

        return len(Stack) == 0
    
        