class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = 0

        for c in s[:k]:
            if c in vowels:
                count += 1

        ans = count
    
        for i in range(k, len(s)):
            count += (s[i] in vowels)
            count -= (s[i-k] in vowels)
            ans = max(ans, count)

        return ans
            
        



        