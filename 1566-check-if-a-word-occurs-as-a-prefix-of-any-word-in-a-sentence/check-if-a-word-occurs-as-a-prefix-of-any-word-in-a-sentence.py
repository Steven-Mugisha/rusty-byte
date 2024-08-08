class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # if len(searchWord) > len(sentence):
        #     return -1
        
        lookUp = sentence.split(" ")
        print(f'lookUp here {lookUp}')

        for word in lookUp:
            if word.startswith(searchWord):
                return lookUp.index(word) + 1
        
        return -1