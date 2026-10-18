class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result=[]
        if len(s)>12:
            return result
        def backtrack(i,dots,string):
            if dots == 4 and i == len(s):
                result.append(string[:-1])
                return
            for j in range(i,min(i+3,len(s))):
                if i!=j and s[i] == "0":
                    continue
                if int(s[i:j+1])<256:
                    backtrack(j+1,dots+1,string+s[i:j+1]+".")
        backtrack(0,0,"")
        return result
        


        # final=[]
        # def backtrack(index,string,comma,initial,character,c):
        #     if(comma >3 or initial>3 or (int(string[:-1])<0 and int(string[:-1])>255)):
        #         return
        #     if(string and string[-1] == "0"):
        #         return 
        #     if(index == len(s)+3):
        #         final.append(string)
        #     backtrack(index+1,string+s[index],comma,initial+1)
        #     backtrack(index+1,string+".",comma+1,initial)
        
        # if len(s) == 12:
        #     return [s[i]+s[i-1]+s[i-2]+"." for i in range(2,len(s)-2) if i%3 == 2]
        # elif len(s) > 12:
        #     return []
        # else:
        #     backtrack(0,"",0,0)
        # return final