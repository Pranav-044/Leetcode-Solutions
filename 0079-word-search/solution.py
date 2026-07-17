class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        index=0
        visited=[[False]*len(board[0]) for _ in range(len(board))]
        def dfs(i, j, index):
            if(i<0 or i>=len(board) or j<0 or j>=len(board[0])):
                return False
            if visited[i][j]:
                return False
            if(board[i][j] != word[index]):
                return False
            if(index == len(word)-1):
                return True
            visited[i][j]=True
            print(board[i][j])
            res=(
            dfs(i-1,j,index+1)
            or dfs(i+1,j,index+1)
            or dfs(i,j+1,index+1)
            or dfs(i,j-1,index+1))
            visited[i][j]=False
            return res
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
        
        
        
        
        
        
        
        # visited=[[False]*len(matrix[0]) for _ in range(len(matrix))]
        # def dfs(row,col,index):
        #     dfs(i,j+1)
        #     dfs(i,j-1)
        #     dfs(i+1,j)
        #     dfs(i-1,j)
        #     if (index == len(board)):
        #         return True
        #     elif(i<0 or i>=len(board) or j<0 or j>=len(board)):
        #         return False
        #     elif(board[i][j]!=board[index]):
        #         return False
            
        
