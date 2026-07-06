class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        count=0
        while l<r:
            if(s[l]!=s[r]):
                left=s[:l]+s[l+1:]
                right=s[:r]+s[r+1:]
                if(left == left[::-1] or right == right[::-1]):
                    return True
                else:
                    return False
            
            else:
                l+=1
                r-=1
        return True
        
