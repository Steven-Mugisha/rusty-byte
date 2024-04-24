class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        res = []
        pc, atl = set(), set()

        def dfs(r,c, visited, prevHeight):
            if (r not in range(rows) or 
                c not in range(cols) or heights[r][c] < prevHeight or 
                (r,c) in visited):
                return 
            
            visited.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, visited, heights[r][c])
    
        for c in range(cols):
            dfs(0, c, pc, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows -1][c])
        
        for r in range(rows):
            dfs(r, 0, pc, heights[r][0])
            dfs(r, cols -1, atl, heights[r][cols -1])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pc and (r,c) in atl:
                    res.append([r,c])
        
        return res