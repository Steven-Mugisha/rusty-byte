class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        N = m*n

        arr = [[0]*n for _ in range(m)]

        for i in range(N):
            j = (i+k)%N
            arr[j//n][j%n] = grid[i//n][i%n]

        return arr
     



        


  