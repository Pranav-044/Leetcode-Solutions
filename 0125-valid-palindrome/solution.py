class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=s.split()
        k=""
        temp=""
        for i in string:
            if not i.isalnum():
                for j in i:
                    if j.isalnum():
                        temp+=j 
                i=temp
                temp=""
            k+=i.lower()
        print(k)
        if(k[::] == k[::-1]):
            return True
        return False
        
