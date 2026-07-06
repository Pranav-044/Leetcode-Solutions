class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        r=len(s)-1
        setter=set("aeiouAEIOU")
        arr=list(s)
        while l<r:
            if(arr[l] in setter and arr[r] in setter):
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            elif(arr[l] in setter and arr[r] not in setter):
                r-=1
            elif(arr[l] not in setter and arr[r] in setter):
                l+=1
            else:
                l+=1
                r-=1
        return "".join(arr)


        
