class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index=0
        if(len(nums)<=1):
            return
        point=-1
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                point=i-1
                break
        
        if(point == -1):
            nums=nums.reverse()
            return nums
        minimum=float("inf")
        for j in range(point,len(nums)):
            if(nums[j]>nums[point]):
                print(j)
                if(nums[j]<minimum or nums[j] == minimum):
                    minimum=nums[j]
                    index=j
        print(nums,minimum,point)
        nums[point],nums[index]=nums[index],nums[point]
        print(nums)
        nums[point+1:]=nums[point+1:][::-1]



        
