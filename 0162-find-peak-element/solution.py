class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if(self.isPeak(mid,nums)):
                return mid
                break
            elif(nums[mid]<nums[mid+1]):
                l=mid+1
            elif(nums[mid]<nums[mid-1]):
                r=mid-1
        
            
    def isPeak(self,mid,nums):
        if(len(nums)==1):
            return True
        if(mid==0):
            if(nums[0]>nums[1]):
                return True
            else:
                return False
        else:
            if(mid==len(nums)-1):
                if(nums[mid]>nums[mid-1]):
                    return True
                else:
                    return False
            else:
                if(nums[mid-1]<=nums[mid] and nums[mid]>=nums[mid+1]):
                    return True
                else:
                    return False
            
                    
        
