class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        current_used_node = self.lookup[key]
        self.remove(current_used_node)
        self.add(current_used_node)

        return current_used_node.val


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            old_node = self.lookup[key]
            self.remove(old_node)
        
        node = LinkedNode(key, value)
        self.lookup[key] = node
        self.add(node)


        if len(self.lookup) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.lookup[node_to_delete.key]
    
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)