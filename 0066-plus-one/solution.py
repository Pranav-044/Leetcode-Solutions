class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=""
        for i in digits:
            k+=str(i)
        final=int(k)+1
        final=list(str(final))
        final=[int(i) for i in final]
        return final


        
