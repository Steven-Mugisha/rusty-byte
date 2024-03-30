class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        island = 0
        seen = set()

        def bfs(r,c):
            queue = [(r,c)]
            seen.add((r,c))

            while queue:
                row, col = queue.pop(0)
                directions = [[1, 0], [-1, 0],[0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (
                        r in range(rows) and c in range(cols) and
                        grid[r][c] == '1' and (r, c) not in seen
                    ):
                        seen.add((r,c))
                        queue.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    island += 1
        
        return island
