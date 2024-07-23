import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for num in nums:
            self.add(num)        

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        
        elif len(self.minHeap) == self.k and self.minHeap[0] < val:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]

# TC: O(logk) and SC: O(k)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)