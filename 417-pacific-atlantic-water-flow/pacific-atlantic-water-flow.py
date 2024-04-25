class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pco, ato = set(), set()
        result = []

        def dfs(r,c, visited, prevHeights):
            if (r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeights or (r,c) in visited):
                return 
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                row, col = dr + r,  dc + c
                dfs(row, col, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pco, heights[0][c])
            dfs(rows-1, c, ato, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pco, heights[r][0])
            dfs(r, cols-1, ato, heights[r][cols-1])
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pco and (r,c) in ato:
                    result.append([r,c])
        
        return result