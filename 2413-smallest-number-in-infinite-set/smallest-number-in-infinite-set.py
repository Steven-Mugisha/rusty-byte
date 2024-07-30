class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.nums = set()
        self.ceiling = 1

    def popSmallest(self) -> int:
        if self.heap:
            sm = heappop(self.heap)
            self.nums.remove(sm)
            return sm
        
        else:
            sm = self.ceiling
            self.ceiling += 1
            return sm
        

    def addBack(self, num: int) -> None:
        if num < self.ceiling and num not in self.nums:
            heappush(self.heap, num)
            self.nums.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)