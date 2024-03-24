class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels =  'aeiou'
        current_str = s[:k]
        total = 0
        for c in current_str:
            if c in vowels:
                total += 1
        ans = total

        for i in range(k, len(s)):
            total += (s[i] in vowels)
            total -= (s[i - k] in vowels)
            ans = max(ans, total)
        
        return ans




