class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        from queue import PriorityQueue

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        pq = PriorityQueue()
        pq.put((0, k))
        seen = set()

        delay_times = 0

        while not pq.empty():
            time, node = pq.get()

            if node in seen:
                continue

            delay_times = max(delay_times, time)
            seen.add(node)
            
            neighbours = graph[node]
            for neighbour, t in neighbours:
                if neighbour not in seen:
                    pq.put((t + time, neighbour))

        if len(seen) == n:
            return delay_times

        return -1



        