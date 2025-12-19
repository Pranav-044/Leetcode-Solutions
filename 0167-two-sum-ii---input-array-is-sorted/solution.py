class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i,n in enumerate(numbers):
            other=target-n
            if other in dict1:
                return ([dict1[other]+1,i+1])
            dict1[n] = i
        
