class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def __get_index(self, char):
        return ord(char) - ord('a')
        
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = self.__get_index(char)
            if current.children[index] == None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.end = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            index = self.__get_index(char)
            if current.children[index] == None:
                return False
            current = current.children[index]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            index = self.__get_index(char)
            if current.children[index] == None:
                return False
            current = current.children[index]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)