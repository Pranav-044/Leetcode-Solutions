class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up=0
        down=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        final=[]
        while up<=down and left<=right:
            for i in range(left,right+1):
                print(matrix[up][i])
                final.append(matrix[up][i])
            up+=1
            for j in range(up,down+1):
                final.append(matrix[j][right])
            right-=1
            if(up<=down):
                for i in range(right,left-1,-1):
                    final.append(matrix[down][i])
                down-=1
            if(left<=right):
                for i in range(down,up-1,-1):
                    final.append(matrix[i][left])
                
                left+=1
        return final



        
