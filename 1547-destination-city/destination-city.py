class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = set()

        for start, end in paths:
            out.add(start)
        
        
        for start, end in paths:
            if end not in out:
                return end
        
        

            


