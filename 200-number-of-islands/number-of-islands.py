class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [
                    [0,1], [0, -1],
                    [1, 0], [-1, 0]
                ]

                for r, c in directions:
                    dr, dc = r + row, c + col
                    if (dr in range(rows) and
                    dc in range(cols) and 
                    (dr, dc) not in visited and 
                    grid[dr][dc] == "1"):
                        queue.append((dr, dc))
                        visited.add((dr,dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
            
        
        return island

            