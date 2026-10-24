class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        before=[]
        after=[]
        equal=0
        for i in range(len(nums)):
            if(nums[i]<pivot):
                before.append(nums[i])
            elif(nums[i] == pivot):
                equal+=1
            else:
                after.append(nums[i])
        return before+[pivot]*equal+after

        