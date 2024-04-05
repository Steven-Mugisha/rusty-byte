from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay_times = 0
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        pq = PriorityQueue()
        pq.put((0,k))
        seen = set()

        while not pq.empty():
            time, node = pq.get()

            if node in seen:
                continue
            
            seen.add(node)
            delay_times = max(delay_times, time)
            neighbors = graph[node]

            for nei,t in neighbors:
                if nei not in seen:
                    pq.put((t + time, nei))
        
        if len(seen) == n:
            return delay_times
        
        return -1 

