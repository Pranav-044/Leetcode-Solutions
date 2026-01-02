class TimeMap:

    def __init__(self):
        self.dictionary=defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
       self.dictionary[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        final_list=self.dictionary[key]
        l,r=0,len(final_list)-1
        val=""
        while l<=r:
            mid=(l+r)//2
            if(final_list[mid][1] == timestamp):
                return final_list[mid][0]
            elif(final_list[mid][1] >timestamp):
                r=mid-1
            else:
                val= final_list[mid][0]
                l=mid+1
        return val
