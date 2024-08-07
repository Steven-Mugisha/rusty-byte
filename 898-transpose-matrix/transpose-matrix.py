class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])

        arr = []

        for c in range(COLS):
            temp = []
            for r in range(ROWS):
                temp.append(matrix[r][c])
            arr.append(temp)
        
        return arr