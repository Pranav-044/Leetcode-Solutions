class Solution:
    def reverseWords(self, s: str) -> str:
        final=s.split()
        return " ".join(final[::-1])
        
