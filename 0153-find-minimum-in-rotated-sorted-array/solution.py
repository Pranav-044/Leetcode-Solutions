class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minimum=0
        mid=0
        while l<r:
            mid=(l+r)//2
            if(nums[mid]>=nums[mid+1]):
                minimum=nums[mid+1]
                return minimum
            elif(nums[mid]<nums[mid+1]):
                if(nums[mid]>nums[-1]):
                    l=mid
                else:
                    r=mid
                    minimum=min(minimum,nums[mid])
        if(l==r):
            return nums[mid]
        return minimum



        
