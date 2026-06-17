class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        s=set(nums)
        for num in s:
            if (num-1) not in s:
                curr=1
                length=1
                while(num+length) in s:
                    length+=1
                    curr+=1
                longest=max(longest,curr)
        return longest


        
