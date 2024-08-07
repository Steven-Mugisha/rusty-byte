class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out_paths, in_paths = set(), set()

        for start, end in paths:
            out_paths.add(start)
            in_paths.add(end)
        
        for end in in_paths:
            if end not in out_paths:
                return end
