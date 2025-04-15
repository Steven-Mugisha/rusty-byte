class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        # swap from top to bottom or the matrix

        for r in range(size >> 1):
            for c in range(size):
                matrix[r][c], matrix[size - r - 1][c] = matrix[size - r - 1][c], matrix[r][c]

        
        for r in range(size):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

                
        
        
        
        
        
        
        
        
        