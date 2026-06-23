class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maximum=0
        # l=0
        # arr=[0]*26
        # for i in range(len(s)):
        #     arr[ord(s[i])-65]+=1
        #     while((i-l+1)-max(arr)>k):
        #         arr[ord(s[l])-65]-=1
        #         l+=1
        #     maximum=max(maximum,i-l+1)
        # return maximum        
        
        
        
        
        
        
        
        
        
        
        dictionary={}
        l=0
        max_f=0
        longest=0
        for i in range(len(s)):
            length=i-l+1
            dictionary[s[i]]=dictionary.get(s[i],0)+1
            max_f=max(max_f,dictionary[s[i]])
            window=length-max_f
            if(window<=k):
                longest=max(longest,length)
                
            else:
                dictionary[s[l]]-=1
                l+=1
        return longest


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # l=0
        # max_f=0
        # dictionary={}
        # maximum=0
        # for i in range(len(s)):
        #     length=i-l+1
        #     dictionary[s[i]]=dictionary.get(s[i],0)+1
        #     max_f=max(dictionary[s[i]],max_f)
        #     val=length-max_f
        #     if(val<=k):
        #         maximum=max(maximum,length)
        #     else:   
        #         dictionary[s[l]]-=1 
        #         l+=1
        # return maximum                

            
        
        
