class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashma={}
        for i in range(len(nums)):
            hashma[nums[i]]=hashma.get(nums[i],0)+1
        for j,k in hashma.items():
            if k == 1:
                return j
            


        
