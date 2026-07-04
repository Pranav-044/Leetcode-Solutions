class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dictionary = {}
        l = 0
        maximum = 0

        for i in range(len(nums)):
            dictionary[nums[i]] = dictionary.get(nums[i], 0) + 1

            while dictionary.get(0, 0) > k:
                dictionary[nums[l]] -= 1
                l += 1

            maximum = max(maximum, i - l + 1)

        return maximum
