from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for i, stations in enumerate(routes):
            for station in stations:
                graph[station].append(i)
        
        q = deque()
        q.append([source, 0])
        seen = set()

        while q:
            station, bus_taken = q.popleft()
            if station == target:
                return bus_taken

            if station in graph:
                for bus in graph[station]:
                    if bus not in seen:
                        seen.add(bus)
                        for s in routes[bus]:
                            q.append([s, bus_taken + 1])
        return -1 
