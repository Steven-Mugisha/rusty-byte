class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq

        freqs = Counter(words)
        heap = []

        for word, fq in freqs.items():
            heapq.heappush(heap, [-fq, word])
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res