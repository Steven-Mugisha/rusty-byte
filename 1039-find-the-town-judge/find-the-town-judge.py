class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1:
            return 1

        trusts = collections.defaultdict(int)
        trusted = collections.defaultdict(int)

        for a,b in trust:
            trusted[b] += 1
            trusts[a] = b
        
        for k,v in trusted.items():
            if v == n - 1 and trusts[k] == 0:
                return k

        return -1 