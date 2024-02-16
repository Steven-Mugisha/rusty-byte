class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        return " ".join(s[::-1])
