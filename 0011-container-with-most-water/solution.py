class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maximum=0
        while l<r:
            content=min(height[l],height[r])*(r-l)
            maximum=max(maximum,content)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maximum


            



            


        
        
