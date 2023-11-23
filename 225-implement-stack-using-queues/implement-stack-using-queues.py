class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

class MyStack:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def push(self, x: int) -> None:
        new_node = Node(x)

        if self.size == 0:
            self.front = new_node
            self.back = new_node
        
        else:
            new_node.next = self.front
            self.front = new_node
        
        self.size += 1
        
    def pop(self) -> int:
        if self.size == 0:
            return None
        
        temp = self.front
        self.front = self.front.next
        temp.next = None

        if self.size == 0:
            self.back = None
        
        self.size -= 1

        return temp.x

    def top(self) -> int:

        if self.size == 0:
            return None
        
        else:
            return self.front.x    

    def empty(self) -> bool:
        return True if not self.size else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()