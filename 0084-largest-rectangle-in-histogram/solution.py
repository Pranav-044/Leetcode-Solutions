class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        prev=[0]*len(heights)
        next_arr=[0]*len(heights)
        max_area=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if stack:
                prev[i]=stack[-1]
            else:
                prev[i]=-1
            stack.append(i)
        stack=[]
        for j in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[j]:
                stack.pop()
            if stack:
                next_arr[j]=stack[-1]
            else:
                next_arr[j]=len(heights)
            
            stack.append(j)
        for k in range(len(heights)):
            area=heights[k]*abs(next_arr[k]-prev[k]-1)
            max_area=max(area,max_area)
        return max_area

        
