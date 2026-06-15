class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        l=0
        final=[]
        for i in range(mid,len(nums)):
            final.append(nums[l])
            final.append(nums[i])
            l+=1
        return final


        
