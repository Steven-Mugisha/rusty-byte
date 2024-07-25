class Solution:
    from collections import Counter
    import heapq
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = []

        for char, count in counter.items():
            maxHeap.append([-count, char])
            heapq.heapify(maxHeap)

        prev = None
        res = ""

        while len(maxHeap) > 0 or prev:
            if len(maxHeap) == 0 and prev:
                return ""
            
            count, char = heapq.heappop(maxHeap)
            res+= char
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]
        
        return res