class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        index=1
        count=1
        current=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]!=current):
                count=1
                current=nums[i]
            else:
                count+=1
            if(count >= 3):
                k+=1
                continue
            nums[index],nums[i] =nums[i],nums[index]
            index+=1
        return len(nums)-k
            


        