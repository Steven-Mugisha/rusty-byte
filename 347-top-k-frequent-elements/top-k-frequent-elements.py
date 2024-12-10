class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freqs = Counter(nums)

        heap = []

        for ele, fq in freqs.items():
            heapq.heappush(heap, [-fq, ele])
        
        results = []
        
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results
    

