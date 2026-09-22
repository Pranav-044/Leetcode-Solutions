class Solution:
    def countArrangement(self, n: int) -> int:
        arr=list(range(1,n+1))
        combinations=[]
        used=[False]*len(arr)
        count=0
        def backtrack(combinations):
            nonlocal count
            if(len(combinations) == n):
                count+=1
                return
            pos=len(combinations)+1
            for i in range(len(arr)):
                if not used[i] and (arr[i]%(pos) == 0 or (pos)%(arr[i]) == 0):
                    used[i] = True
                    backtrack(combinations+[arr[i]])
                    used[i] = False 
        backtrack([])
        return count
        
