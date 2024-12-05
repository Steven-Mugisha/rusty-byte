class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        indegree = set()
        outdegree = set()

        for start, end in paths:
            outdegree.add(start)
            indegree.add(end)
        
        for i in indegree:
            if i not in outdegree:
                return i
            