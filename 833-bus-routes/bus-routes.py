class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        connections = defaultdict(list)
        for i, stations in enumerate(routes):
            for station in stations:
                connections[station].append(i)
        
        seen = set()
        q = deque()
        q.append([source, 0])

        while q:
            station, bus_taken = q.popleft()
            if station == target:
                return bus_taken
            
            if station in connections:
                for bus in connections[station]:
                    if bus not in seen:
                        for st in routes[bus]:
                            q.append([st, bus_taken + 1])
                        seen.add(bus)
        return -1

