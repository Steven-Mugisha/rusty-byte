class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = defaultdict(int)

        for v,e in edges:
            graph[v] += 1
            graph[e] += 1
        
        for k,v in graph.items():
            if v == len(graph) - 1:
                return k