class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftMax=[0]*(len(height))
        rightMax=[0]*(len(height))
        lMax=0
        rMax=0
        total=0
        leftMax[0] = 0
        rightMax[(len(height)-1)] = 0
        for i in range(len(height)):
            leftMax[i] = lMax
            lMax=max(lMax,height[i])
        for j in range(len(height)-1,-1,-1):
            rightMax[j] = rMax
            rMax=max(rMax,height[j])
        for k in range(1,len(height)-1):
            temp=min(leftMax[k],rightMax[k]) - height[k]
            if (temp>0):
                total+=temp
        
        return total
        
