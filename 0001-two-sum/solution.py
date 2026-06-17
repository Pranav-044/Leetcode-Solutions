class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final={}
        for i,j in enumerate(nums):
            final[j]=i
          
        for k in range(len(nums)):
            if target-nums[k] in final and final[target-nums[k]]!=k:
                return [k,final[target-nums[k]]]

