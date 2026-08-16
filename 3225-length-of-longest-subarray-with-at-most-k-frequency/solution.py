class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dictionary={}
        l=0
        final=0
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]]=1
            else:
                dictionary[nums[i]]+=1
            if dictionary[nums[i]]<=k:
                final=max(final,i-l+1)
            else:
                while(l<=i and dictionary[nums[i]]>k):
                    dictionary[nums[l]]-=1
                    l+=1
                
        return final




        
