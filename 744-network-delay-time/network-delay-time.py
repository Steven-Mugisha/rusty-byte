from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = defaultdict(list)

        for u,v,w in times:
            connections[u].append([v, w])
        
        seen, delay_times = set(), 0

        pq = PriorityQueue()
        pq.put([0, k])

        while not pq.empty():
            time, node = pq.get()

            if node in seen:
                continue
            
            seen.add(node)
            delay_times = max(delay_times, time)
            neighbors = connections[node]

            for v,t in neighbors:
                if v not in seen:
                    pq.put([t + time, v])

        if len(seen) == n:
            return delay_times        

        return -1