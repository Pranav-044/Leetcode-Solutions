class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        i=0
        p=True
        nums1=[]
        nums2=[]
        while(i<len(nums)):
            if(p):
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
            p = not  p
            if(nums1 and nums2 and nums1[-1]>nums2[-1]):
                p = True
            else:
                p = False
            i+=1
        return nums1+nums2
            
        
