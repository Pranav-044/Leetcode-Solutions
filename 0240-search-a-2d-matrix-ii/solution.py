class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(line):
            l=0
            r=len(line)-1
            while l<=r:
                mid=(l+r)//2
                if(line[mid] == target):
                    return True
                elif(line[mid]>target):
                    r=mid-1
                else:
                    l=mid+1
            return False
        r=len(matrix)
        for i in range(r):
            if search(matrix[i]):
                return True
        return False
        
        
