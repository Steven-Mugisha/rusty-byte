class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        sentence = sentence.split(" ")
        for idx, word in enumerate(sentence):
            if word.startswith(searchWord):
                return idx + 1
        
        return -1 