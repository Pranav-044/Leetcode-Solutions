class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        final=[]
        while(l<=r):
            if(abs(nums[l]**2)>abs(nums[r]**2)):
                final.append(abs(nums[l]**2))
                l+=1
            else:
                final.append(abs(nums[r]**2))
                r-=1
        return final[::-1]

        
