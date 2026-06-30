class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if(n <= 1):
            return n

        dp = [1] * n
        parent = [-1] * n
        max_len = 0

        for i in range(1, n):
            for j in range(i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    parent[i] = j

            max_len = max(max_len, dp[i])

        # index = dp.index(max_len)
        # res = []
        # while index != -1:
        #     res.append(arr[index])
        #     index = parent[index]
        # res.reverse()

        return max_len
        
