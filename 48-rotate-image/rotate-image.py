class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r - l):
                t, b = l, r
                tl = matrix[t][l+i]

                # top left:
                matrix[t][l+i] = matrix[b-i][l]
                # bottom left:
                matrix[b-i][l] = matrix[b][r-i]
                # bottom right:
                matrix[b][r-i] = matrix[t+i][r]
                # top right
                matrix[t+i][r] = tl
            
            r -= 1
            l += 1

