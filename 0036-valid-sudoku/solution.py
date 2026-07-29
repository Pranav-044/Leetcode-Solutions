class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            setter=set()
            for j in range(len(board[0])):
                if board[i][j] in setter:
                    return False
                elif board[i][j] !=".":
                    setter.add(board[i][j])
        for i in range(len(board[0])):
            setter=set()
            for j in range(len(board)):
                if board[j][i] in setter:
                    return False
                elif board[j][i] !=".":
                    setter.add(board[j][i])
        start=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i,j in start:
            setter=set()
            for row in range(i,i+3):
                for cols in range(j,j+3):
                    if board[row][cols] in setter:
                        return False
                    elif board[row][cols] !=".":
                        setter.add(board[row][cols])
        
        return True


