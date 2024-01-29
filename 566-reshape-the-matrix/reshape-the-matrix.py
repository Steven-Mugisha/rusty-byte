class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        reshapedMat = [[0 for _ in range(c)] for _ in range(r)]
        m, n = len(mat), len(mat[0])

        # check if the transformation if possible
        if m*n != r*c:
            return mat

        # flatten mat:
        _1dmat = []
        for i in range(m):
            for j in range(n):
                _1dmat.append(mat[i][j])
        
        # added _1dmat values to reshapedMat
        k = 0
        for x in range(r):
            for y in range(c):
                reshapedMat[x][y] = _1dmat[k]
                k += 1
        
        return reshapedMat


        

        




    



        


        