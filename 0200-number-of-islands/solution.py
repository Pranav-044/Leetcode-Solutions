class Solution:
    def dfs(self,i,j,m,n,grid):
        if(i<0 or i>=m or j<0 or j>=n or grid[i][j]!="1"):
            return
        else:
            grid[i][j]="0"
            self.dfs(i,j+1,m,n,grid)
            self.dfs(i,j-1,m,n,grid)
            self.dfs(i+1,j,m,n,grid)
            self.dfs(i-1,j,m,n,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        islands=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands+=1
                    self.dfs(i,j,m,n,grid)
        return islands

        
