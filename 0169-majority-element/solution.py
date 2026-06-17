class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        majority_threshold = len(nums) // 2
        for num, count in hashmap.items():
            if count > majority_threshold:
                return num
