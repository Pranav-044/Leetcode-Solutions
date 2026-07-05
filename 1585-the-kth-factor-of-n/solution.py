class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small=[]
        longest=[]
        for i in range(1,int(n**0.5)+1):
            if(n%i==0):
                small.append(i)
                if(n//i != i):
                    longest.append(n//i)
        res=small+longest[::-1]
        if((k-1)>=len(res)):
            return -1
        return res[k-1]
        
