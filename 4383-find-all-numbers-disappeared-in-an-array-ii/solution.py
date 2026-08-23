class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        setter=set(nums)
        final=[]
        arr=[]
        start=-1
        end=-1
        for i in range(lower,upper+1):
            if(i not in setter):
                if(start==-1):
                    start=i
                end=i
            if(i in setter or i == upper):
                if(start!=-1 and end!=-1):
                    final.append([start,end])
                start=-1
        
        return final
                
        
        
