

# 20. Valid Parentheses

# summary: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# key words: string, characters, determine, valid, open brackets, closed brackets, same type, correct order

class Solution:
    def isValid(self, s: str) -> bool:
        
        closing_char = {"}":"{", ")":"(", "]":"["}
        stack = []

        for c in s:
            if c in closing_char:
                if stack and stack[-1] == closing_char[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

# Time complexity: O(n)
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true



