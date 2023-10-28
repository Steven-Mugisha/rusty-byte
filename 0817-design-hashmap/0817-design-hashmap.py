class ListNode:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hashfunc(self, key):
        hash = key % len(self.map)
        return hash 

    def put(self, key: int, value: int) -> None:
        index = self.hashfunc(key)
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return 
            cur = cur.next
        cur.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        index = self.hashfunc(key)
        cur = self.map[index].next

        while cur and cur.key != key:
            cur = cur.next
        if cur:
            return cur.val
        return -1


    def remove(self, key: int) -> None:
        index = self.hashfunc(key)
        cur = self.map[index]

        while cur.next and cur.next.key != key:
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next 
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)