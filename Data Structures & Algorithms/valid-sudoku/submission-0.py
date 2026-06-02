class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board))]
        grids = [[] for _ in range(len(board))]
        
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col].isdigit():
                    if (board[row][col] in rows[row] or \
                        board[row][col] in cols[col] or \
                        board[row][col] in grids[int((row // 3) * 3 + (col // 3 ))]):

                        return False

                    rows[row].append(board[row][col])
                    cols[col].append(board[row][col])
                    grids[int((row // 3) * 3 + (col // 3))].append(board[row][col])
        return True

        