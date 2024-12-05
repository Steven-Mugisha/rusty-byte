class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict

        # outbounds = defaultdict()
        # inbounds = defaultdict()
        outbounds, inbounds = set(), set()
        

        for idx, path in enumerate(paths):
            start, dest = path
            outbounds.add(start)
            inbounds.add(dest)
        
        for city in inbounds:
            if city not in outbounds:
                return city