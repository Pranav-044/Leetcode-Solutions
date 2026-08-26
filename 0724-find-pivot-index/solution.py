class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_pref=[0]*len(nums)
        r_pref=[0]*len(nums)
        summation=0
        for i in range(len(nums)):
            l_pref[i] = summation
            summation+=nums[i]
        summation=0
        for j in range(len(nums)-1,-1,-1):
            r_pref[j] = summation
            summation+=nums[j]
        print(l_pref,r_pref)
        for k in range(len(nums)):
            if(l_pref[k] == r_pref[k]):
                return k
        return -1
        
