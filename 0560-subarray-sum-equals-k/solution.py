class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        pref_sum=0
        for i in nums:
            pref_sum+=i
            count+=hashmap.get(pref_sum-k,0)
            hashmap[pref_sum]=hashmap.get(pref_sum,0)+1
            
        return count
        
