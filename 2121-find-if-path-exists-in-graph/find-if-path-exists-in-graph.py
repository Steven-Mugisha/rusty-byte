class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        my_graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            my_graph[u].append(v)
            my_graph[v].append(u) 
        
        queue = [source]
        visited = set()

        while queue:
            curr_vertex = queue.pop(0)
            if curr_vertex == destination:
                return True
            
            if curr_vertex not in visited:
                visited.add(curr_vertex)
                for neighbor in my_graph[curr_vertex]:
                    queue.append(neighbor)
        
        return False
        