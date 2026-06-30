class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMax=[-1]*n
        rightMax=[-1]*n
        val=0
        leftMaximum=float("-inf")
        rightMaximum=float("-inf")
        for i in range(len(height)):
            if(height[i]>leftMaximum):
                leftMaximum=height[i]    
            leftMax[i]=leftMaximum
        for j in range(n-1,-1,-1):
            if(height[j]>rightMaximum):
                rightMaximum=height[j]
            rightMax[j]=rightMaximum
        for k in range(1,n):
            val+=min(leftMax[k],rightMax[k])-(height[k])
        return val



        
        

































































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
        
