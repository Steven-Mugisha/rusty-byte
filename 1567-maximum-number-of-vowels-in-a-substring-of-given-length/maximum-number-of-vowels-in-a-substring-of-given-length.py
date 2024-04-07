class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        currCount = sum(1 for char in s[:k] if char in vowels)

        res = currCount

        for i in range(k, len(s)):
            currCount += (1 if s[i] in vowels else 0)
            currCount -= (1 if s[i-k] in vowels else 0)

            res = max(res, currCount)
        
        return res
    