class Solution:
    def isPalindromic(self, s: str) -> bool:
        final=""
        def Binary(val):
            string=""
            while(val!=0):
                if(val%2 == 0):
                    string+="0"
                else:
                    string+="1"
                val//=2
            string=string[::-1]
            while(len(string)<8):
                string="0"+string
            return string
        for i in s:
            final+=Binary(ord(i))
        if(final == final[::-1]):
            return True
        return False
            
                    
        
