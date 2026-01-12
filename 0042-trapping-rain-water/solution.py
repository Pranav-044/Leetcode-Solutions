class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[]
        right_max=[0]*len(height)
        l_max=0
        r_max=0
        final=0
        for i in range(len(height)):
            left_max.append(l_max)
            l_max=max(l_max,height[i])
        for j in range(len(height)-1,-1,-1):
            right_max[j]=r_max
            r_max=max(r_max,height[j])
        for k in range(len(height)):
            res=min(left_max[k],right_max[k])-height[k]
            if(res>0):
                final+=res
        return final

        

































































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
        
