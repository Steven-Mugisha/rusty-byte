class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        connections = defaultdict(list)

        for bus, stations in enumerate(routes):
            for station in stations:
                connections[station].append(bus)

        q = deque()
        q.append([source, 0])
        seen = set()

        while q:
            station, buses_taken = q.popleft()
            if station == target:
                return buses_taken
            
            if station in connections:
                for bus in connections[station]:
                    if bus not in seen:
                        for st in routes[bus]:
                            q.append([st, buses_taken + 1])
                        seen.add(bus)

        return -1



