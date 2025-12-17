import heapq
from bisect import bisect_left

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free=list(range(k))
        busy=[]
        count=[0]*k

        for i in range(len(arrival)):
            time=arrival[i]
            while busy and busy[0][0]<=time:
                end,server=heapq.heappop(busy)
                idx=bisect_left(free,server)
                free.insert(idx,server)
            if not free:
                continue
            start=i%k
            idx=bisect_left(free,start)
            if (idx==len(free)):
                idx=0
            server=free.pop(idx)

            heapq.heappush(busy,(time+load[i],server))
            count[server]+=1
        max_req=max(count)
        return [i for i,c in enumerate(count) if c==max_req]



        
       
