class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def search_word(x, y, index):

            if index == len(word)-1:
                return board[x][y] == word[index]
            
            if board[x][y] != word[index]:
                return False
            
            temp = board[x][y]
            board[x][y] = "0"

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if new_x in range(ROWS) and new_y in range(COLS) and board[new_x][new_y] != "0":
                    if search_word(new_x, new_y, index + 1):
                        return True
            
            board[x][y] = temp
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and search_word(r, c,0):
                    return True
        
        return False