class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        check=False
        while l<=r:
            mid=(l+r)//2
            if(matrix[mid][-1]>=target and matrix[mid][0]<=target):
                check=solve(0,len(matrix[mid])-1,matrix[mid],target)
                break
            
            elif(matrix[mid][-1]<target):
                l=mid+1
            else:
                r=mid-1
        return check
        

def solve(l,r,arr,target):
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]<target):
            l=mid+1
        elif(arr[mid]>target):
            r=mid-1
        else:
            return True
    return False

