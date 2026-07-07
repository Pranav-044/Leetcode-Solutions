class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l=0
        r=0
        peak=False
        maximum=0
        for i in range(1,len(arr)-1):
            if(arr[i-1]<arr[i]>arr[i+1]):
                l=r=i
                while l>0:
                    if(arr[l]>arr[l-1]):
                        l-=1
                    else:
                        break
                while(r<len(arr)-1):
                    if(arr[r]>arr[r+1]):
                        r+=1
                    else:
                        break
                maximum=max(maximum,r-l+1)
        return maximum
        
