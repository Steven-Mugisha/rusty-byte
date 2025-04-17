class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, cols = len(matrix), len(matrix[0])


        leftCol, rightCol = 0, cols - 1
        topRow, bottomRow = 0, rows - 1
        res = []


        while (topRow) <= (bottomRow) and (leftCol) <= (rightCol):
            
            # copy top row:
            for i in range(leftCol, rightCol + 1):
                res.append(matrix[topRow][i])
            topRow += 1

            # copy right hand col

            for i in range(topRow, bottomRow + 1):
                res.append(matrix[i][rightCol])
            
            rightCol -= 1

            # copy bottom row
            if (topRow <= bottomRow):
                for i in range(rightCol, leftCol-1, -1):
                    res.append(matrix[bottomRow][i])
                bottomRow -= 1
            
            # copy left hand col

            if (leftCol <= rightCol):
                for i in range(bottomRow, topRow-1, -1):
                    res.append(matrix[i][leftCol])
                leftCol += 1
        
        return res
        



