class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # topleft:
                topLeft = matrix[top][left+i]

                #topLeft:
                matrix[top][left+i] = matrix[bottom-i][left]

                # bottomleft:
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # bottomright:
                matrix[bottom][right-i] = matrix[top+i][right]

                # topright:
                matrix[top+i][right] = topLeft
            
            right -= 1
            left += 1

