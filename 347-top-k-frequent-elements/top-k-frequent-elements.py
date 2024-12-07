class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = Counter(nums)
        top_k_elements = []

        for n, fq in frequencies.items():
            heapq.heappush(top_k_elements, [-fq, n])
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(top_k_elements)[1])
        
        return result
