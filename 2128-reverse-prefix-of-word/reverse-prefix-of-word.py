class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l, res = 0,  list(word)
        for r in range(len(word)):
            if res[r] == ch:
                while l <= r:
                    res[l], res[r] = res[r], res[l]
                    l += 1
                    r -= 1
                return "".join(res)
        return word
        
        