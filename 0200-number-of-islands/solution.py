class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        def dfs(i,j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == 0):
                return
            if(grid[i][j] == "1"):
                grid[i][j] = "0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    dfs(i,j)
                    count+=1
        return count






        # i_count=0
        # count=0
        # def dfs(i,j,grid):
        #     nonlocal count
        #     if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == "0"):
        #         return
        #     if(grid[i][j] == "1"):
        #         count+=1
        #         grid[i][j] = "0"
        #     dfs(i+1,j,grid)
        #     dfs(i,j+1,grid)
        #     dfs(i-1,j,grid)
        #     dfs(i,j-1,grid)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if(grid[i][j] == "1"):
        #             dfs(i,j, grid)
        #             i_count+=1
        # return i_count

    # def dfs(self,i,j,m,n,grid):
    #     if(i<0 or i>=m or j<0 or j>=n or grid[i][j]!="1"):
    #         return
    #     else:
    #         grid[i][j]="0"
    #         self.dfs(i,j+1,m,n,grid)
    #         self.dfs(i,j-1,m,n,grid)
    #         self.dfs(i+1,j,m,n,grid)
    #         self.dfs(i-1,j,m,n,grid)

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     m=len(grid)
    #     n=len(grid[0])
    #     islands=0
        
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 islands+=1
    #                 self.dfs(i,j,m,n,grid)
    #     return islands

        
