class Solution:
    def frequencySort(self, s: str) -> str:
        lookup = Counter(s)

        max_heap = []

        for key, val in lookup.items():
            heappush(max_heap, (-val, key))
        
        res = []

        while max_heap:
            count, char = heappop(max_heap)
            res.append(char * (-count))
        
        return "".join(res)