class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:

            if len(stack) != 0 and c =='*':
                stack.pop()
            
            else:
                stack.append(c)
            
        return "".join(stack)
        





