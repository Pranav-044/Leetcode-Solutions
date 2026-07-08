class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float("-inf")
        current_sum=0
        if(len(nums) == 1):
                return nums[0]
        for i in range(len(nums)):
            current_sum+=nums[i]
            maximum=max(maximum,current_sum)
            if(current_sum<0):
                current_sum=0
            
            
        return maximum
        
