class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))

            perims = dfs(i, j+1)
            perims += dfs(i+1, j)
            perims += dfs(i, j-1)
            perims += dfs(i-1, j)

            return perims

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r, c)


            


