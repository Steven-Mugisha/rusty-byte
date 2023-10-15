class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix)-1 
        
        while l < r:
            for i in range (r - l):
                top, bottom = l, r
                
                # keep the topleft value:
                topLeft = matrix[top][l+i]
                
                # move the bottom left into topleft
                matrix[top][l+i] = matrix[bottom-i][l]
                
                # move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # move top right into bottom right 
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # place topLeft into top right
                matrix[top+i][r] = topLeft
                
            r -= 1
            l += 1
            
            
        
        
        
        
        
        