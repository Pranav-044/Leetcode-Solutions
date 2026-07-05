class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            lcm=1
            for j in range(i,len(nums)):
                lcm=((lcm*nums[j]))//gcd(nums[j],lcm)
                if(lcm == k):
                    count+=1
                elif(lcm>k or k%lcm!=0):
                    break
        return count

        
