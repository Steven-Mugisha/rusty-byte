class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        island, visited = 0, set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [(1,0), (-1, 0), (0, 1), (0,-1)]

                for dr, dc in directions :
                    R,C = row + dr,  col + dc

                    if (R in range(ROWS) and C in range(COLS) and (R,C) not in visited and grid[R][C] == "1"):
                        visited.add((R, C))
                        q.append((R,C))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    island += 1
        return island