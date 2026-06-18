class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ins_index=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[ins_index],nums[i]=nums[i],nums[ins_index]
                ins_index+=1
        return nums        
                

        """
        Do not return anything, modify nums in-place instead.
        """
        
