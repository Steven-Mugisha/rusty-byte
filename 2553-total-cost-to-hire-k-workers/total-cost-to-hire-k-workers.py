class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []

        for i in range(candidates):
            heappush(heap, (costs[i], 0))
        
        for j in range(max(candidates, len(costs) - candidates), len(costs)):
            heappush(heap, (costs[j], 1))
        
        res = 0
        left = candidates
        right = len(costs) - candidates - 1

        for _ in range(k):
            min_cost, direction = heappop(heap)
            res += min_cost
            if left <= right:
                if direction == 0:
                    heappush(heap, (costs[left], 0))
                    left += 1
                
                else:
                    heappush(heap, (costs[right], 1))
                    right -= 1
        
        return res
