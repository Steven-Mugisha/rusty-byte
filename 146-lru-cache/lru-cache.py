class LinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = LinkedNode(-1,-1)
        self.tail = LinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if not key in self.dic:
            return -1
        
        current_node = self.dic[key]
        self.remove_node(current_node)
        self.add_node(current_node)

        return current_node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove_node(old_node)
        
        node = LinkedNode(key, value)
        self.dic[key] = node
        self.add_node(node)

        if len(self.dic) > self.capacity:
            delete_node = self.head.next
            self.remove_node(delete_node)
            del self.dic[delete_node.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)