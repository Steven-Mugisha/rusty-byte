class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        out_going,in_coming = set(), set()

        for start, dest in paths:
            out_going.add(start)
            in_coming.add(dest)
    
        for city in in_coming:
            if city not in out_going:
                return city
        