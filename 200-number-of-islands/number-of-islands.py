class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        island, visited = 0, set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == '1' and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    island += 1
        
        return island