class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                t,b = left, right

                tLeft = matrix[t][left+i]
                matrix[t][left+i] = matrix[b-i][left]
                matrix[b-i][left] = matrix[b][right-i]
                matrix[b][right-i] = matrix[t+i][right]

                matrix[t+i][right] = tLeft
            
            right -= 1
            left += 1
        
        
        
        
        
        