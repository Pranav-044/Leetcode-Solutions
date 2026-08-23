class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def Prime(number: int) -> set:
              setter = set()
              for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                  setter.add(i)
                  while number % i == 0:
                    number //= i
              if number > 1:
                setter.add(number)
              return setter
        
        memo = {}
        for num in nums:
          if num not in memo:
            memo[num] = Prime(num)
        freq = {}
        l = 0
        max_len = 0
        for r in range(len(nums)):
          for p in memo[nums[r]]:
            freq[p] = freq.get(p, 0) + 1
          while len(freq) > k:
            for p in memo[nums[l]]:
              freq[p] -= 1
              if freq[p] == 0:
                del freq[p]
            l += 1
          max_len = max(max_len, r - l + 1)
        return max_len
                
        
