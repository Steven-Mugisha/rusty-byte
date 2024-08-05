class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap, ans = [], []

        for word, count in freq.items():
            heappush(heap, (-count, word))
        
        for i in range(k):
            top_freq_word = heappop(heap)
            ans.append(top_freq_word[1])
        
        return ans
