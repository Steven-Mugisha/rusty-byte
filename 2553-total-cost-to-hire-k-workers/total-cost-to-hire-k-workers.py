class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        minHeap = []

        for i in range(candidates):
            heappush(minHeap, (costs[i], 0))
        
        for j in range(max(candidates, len(costs) - candidates), len(costs)):
            heappush(minHeap, (costs[j], 1))
        
        ans = 0
        left = candidates
        right = len(costs) - candidates - 1

        for _ in range(k):
            min_cost, direction = heappop(minHeap)
            ans += min_cost

            if left <= right:
                if direction == 0:
                    heappush(minHeap, (costs[left], 0))
                    left += 1
                else:
                    heappush(minHeap, (costs[right], 1))
                    right -= 1
        
        return ans
