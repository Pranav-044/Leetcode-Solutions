class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maximum=0
        while l<r:
            capacity=(r-l)*(min(height[l],height[r]))
            maximum=max(capacity,maximum)
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return maximum

            



            


        
        
