class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freqs = Counter(nums)
        heap = []

        for n, fq in freqs.items():
            heapq.heappush(heap, [-fq, n])
        
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans

