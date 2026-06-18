class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ins_index=0
        count=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[ins_index],nums[i]=nums[i],nums[ins_index]
                ins_index+=1
        return ins_index 
        
