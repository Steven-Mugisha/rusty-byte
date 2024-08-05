class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # first count the frequency into a map:
        freq = Counter(nums)
        heap = []
        ans = []

        for n, fq in freq.items():
            heappush(heap, (- fq, n))
        
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans








