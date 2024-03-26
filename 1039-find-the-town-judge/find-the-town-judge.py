class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for trusts, trusted in trust:
            indegree[trusted] += 1
            outdegree[trusts] += 1
        

        for v, k in indegree.items():
            if k == n-1 and outdegree[v] == 0:
                return v
        
        return - 1
        
