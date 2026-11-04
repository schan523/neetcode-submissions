class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            visited = [False] * 10
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if visited[int(board[i][j])]:
                        return False
                    else:
                        visited[int(board[i][j])] = True

        # columns
        for i in range(9):
            visited = [False] * 10
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    if visited[int(board[j][i])]:
                        return False
                    else:
                        visited[int(board[j][i])] = True

        # grids
        for i in range(3):
            for j in range(3):
                visited = [False] * 10
                for k in range(3):
                    for l in range(3):
                        x, y = i*3 + k, j*3 + l  
                        if board[x][y] == ".":
                            continue
                        else:
                            if visited[int(board[x][y])]:
                                return False
                            else:
                                visited[int(board[x][y])] = True
        
        return True