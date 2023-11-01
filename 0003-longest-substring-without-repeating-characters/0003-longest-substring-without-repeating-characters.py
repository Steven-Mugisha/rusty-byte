class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        MaxLength = 0
        Mapset = set()
        windowStart = 0


        for windowEnd in range(len(s)):
            while s[windowEnd] in Mapset:
                Mapset.remove(s[windowStart])
                windowStart += 1

            Mapset.add(s[windowEnd])

            MaxLength = max(MaxLength, windowEnd - windowStart + 1)

        return MaxLength

