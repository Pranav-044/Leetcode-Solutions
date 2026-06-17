class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[0]*len(nums)
        left=[1]*len(nums)
        prod_left=1
        prod_right=1
        right=[1]*len(nums)
        for i in range(len(nums)):
            left[i]=prod_left
            prod_left*=nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            right[j]=prod_right
            prod_right*=nums[j] 
        print(right)
        print(left)        
        for k in range(len(nums)):
            final[k]=left[k]*right[k]
        return final
        
