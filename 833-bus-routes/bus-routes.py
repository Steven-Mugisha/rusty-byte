class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)

        for bus, stations in enumerate(routes):
            for station in stations:
                graph[station].append(bus)
        
        seen = set()

        q = deque()
        q.append([source, 0])

        while q:
            station, buses_taken = q.popleft()
            if station == target:
                return buses_taken
            
            for bus in graph[station]:
                if bus not in seen:
                    seen.add(bus)
                    for st in routes[bus]:
                        q.append([st, buses_taken + 1])
        return -1