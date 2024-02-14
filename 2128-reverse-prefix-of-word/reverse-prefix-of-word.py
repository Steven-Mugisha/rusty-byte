class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l, wordList = 0, list(word)

        for r in range(len(word)):
            if word[r] == ch:
                while l < r:
                    wordList[l], wordList[r] = wordList[r], wordList[l]
                    l += 1
                    r -= 1
                return "".join(wordList)
        
        return word
        
        