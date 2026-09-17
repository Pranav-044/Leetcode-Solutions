class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ans=0
        extra=[]
        zeros=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    zeros.append([i,j])
                elif(grid[i][j]>1):
                    for _ in range(grid[i][j]-1):
                        extra.append([i,j])
        used=[False]*(len(zeros))
        def dfs(index):
            ans=float("inf")
            if(index == len(extra)):
                return 0
            r,s=extra[index]
            for y in range(len(zeros)):
                if(used[y]):
                    continue
                used[y] = True
                i,j=zeros[y]
                distance=abs(r-i)+abs(s-j)
                ans=min(ans,distance+dfs(index+1))
                used[y]=False
            return ans

        return dfs(0)    
