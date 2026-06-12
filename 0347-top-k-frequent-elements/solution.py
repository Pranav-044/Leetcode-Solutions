class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary={}
        final=[]
        bucket=[[] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            dictionary[nums[i]]=dictionary.get(nums[i],0)+1
        print(dictionary)    
        for l,r in dictionary.items():
            bucket[r].append(l)
        print(bucket)    
        for j in range(len(bucket)-1,-1,-1):
            if(k!=0 and bucket[j]!=[]):
                if(len(bucket[j])>1):
                    for l in range(len(bucket[j])):
                        if(k!=0):
                            final.append(bucket[j][l])
                            k-=1

                else:
                    final.append(bucket[j][0])
                    k-=1
        return final


        
        
        
        
        
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dictionary={}
        # j=0
        # q=[]
        # final=[[] for i in range(len(nums)+1)]
        # for i in nums:
        #     dictionary[i]=dictionary.get(i,0)+1
        # for l,p in dictionary.items():
        #     final[p].append(l)
        # for m in range(len(final)-1,-1,-1):
        #     if(j!=k and final[m]!=[]):
        #         j+=len(final[m])
        #         q+=final[m]
        # return q

        

