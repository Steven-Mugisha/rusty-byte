class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pc , at = set(), set()
        result = []

        def dfs(r,c, visited, prevHeights):
            if (r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prevHeights or (r,c) in visited):
                return 
            
            visited.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pc, heights[0][c])
            dfs(ROWS-1, c, at, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pc, heights[r][0])
            dfs(r, COLS-1, at, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pc and (r,c) in at:
                    result.append([r,c])
        return result


        