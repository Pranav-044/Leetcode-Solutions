class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j]!=".":
                    s.add(board[i][j])
        
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i]!=".":
                    s.add(board[j][i])
        
        
        
        indices=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for j,k in indices:
            s=set()
            for i in range(j,j+3):
                
                for m in range(k,k+3):
                    if board[i][m] in s:
                        return False
                    elif board[i][m]!=".":
                        s.add(board[i][m])
        return True

        

