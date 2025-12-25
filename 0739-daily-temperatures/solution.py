class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,l in enumerate(temperatures):
            while stack and l>stack[-1][0]:
                elem,idx=stack.pop()
                res[idx] = (i-idx)
            stack.append([l,i])
        return res
        
