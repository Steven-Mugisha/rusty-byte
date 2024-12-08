class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        freqs = Counter(s)
        heap = []

        for char, fq in freqs.items():
            heapq.heappush(heap, [-fq, char])
        
        previous = None
        result = ""
        while len(heap) > 0 or previous:
            if len(heap) == 0 and previous:
                return ""
            
            count, char = heapq.heappop(heap)
            count += 1

            result += char

            if previous:
                heapq.heappush(heap, previous)
                previous = None
            
            if count != 0:
                previous = [count, char]
        
        return result