class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bot=len(matrix)-1
        while top<=bot:
            mid=(top+bot)//2
            if (matrix[mid][-1]<target):
                top=mid+1
            elif(matrix[mid][0]>target):
                bot=mid-1
            else:
                break
        if(not (top<=bot)):
            return False
        l=0
        r=len(matrix[mid])
        while l<=r:
            temp_mid=(l+r)//2
            if(matrix[mid][temp_mid]==target):
                return True
            elif(matrix[mid][temp_mid]>target):
                r=temp_mid-1
            elif(matrix[mid][temp_mid]<target):
                l=temp_mid+1
        return False
        
