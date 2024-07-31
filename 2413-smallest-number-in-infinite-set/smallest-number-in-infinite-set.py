class SmallestInfiniteSet:

    def __init__(self):
        self.num_set = set()
        self.heap = []
        self.SmallestFromInfSet = 1

    def popSmallest(self) -> int:
        if self.heap:
            sm = heappop(self.heap)
            self.num_set.remove(sm)
            return sm
        
        else:
            sm = self.SmallestFromInfSet
            self.SmallestFromInfSet += 1
            return sm
        
    def addBack(self, num: int) -> None:
        if num not in self.num_set and num < self.SmallestFromInfSet:
            heappush(self.heap, num)
            self.num_set.add(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)