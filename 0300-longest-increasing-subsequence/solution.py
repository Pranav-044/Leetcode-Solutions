class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if(n <= 1):
            return n
        max_len=0
        dp=[1]*n
        parent=[-1]*n
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i]>nums[j]):
                    dp[i]=max(dp[i],dp[j]+1)
            max_len=max(max_len,dp[i])
        return max_len

        # index = dp.index(max_len)
        # res = []
        # while index != -1:
        #     res.append(arr[index])
        #     index = parent[index]
        # res.reverse()

        
        
