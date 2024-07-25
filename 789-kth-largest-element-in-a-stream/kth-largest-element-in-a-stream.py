import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.topK_elements = []

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.topK_elements) < self.k:
            heapq.heappush(self.topK_elements,val)
        
        elif len(self.topK_elements) == self.k and self.topK_elements[0] < val:
            heapq.heappop(self.topK_elements)
            heapq.heappush(self.topK_elements, val)
        
        return self.topK_elements[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)