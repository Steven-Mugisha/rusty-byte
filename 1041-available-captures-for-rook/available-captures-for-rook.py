class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r, c = len(board), len(board[0])

        ROOK = []
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'R':
                    ROOK = [i, j]
                    break
        x, y = ROOK[0], ROOK[1]

        count = 0

        # left:
        for i in range(x-1, -1, -1):
            if board[i][y] == 'p':
                count += 1
                break
            elif board[i][y] == 'B':
                break

        # right:
        for i in range(x+1, 8):
            if board[i][y] == 'p':
                count += 1
                break
            elif board[i][y] == 'B':
                break

        # bottom:
        for i in range(y-1, -1 , -1):
            if board[x][i] == 'p':
                count += 1
                break
            elif board[x][i] == 'B':
                break
        
        # top:
        for i in range(y+1, 8):
            if board[x][i] == 'p':
                count += 1
                break
            elif board[x][i] == 'B':
                break
        
        return count

