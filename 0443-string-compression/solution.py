class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0
        n=len(chars)
        while read<n:
            current=chars[read]
            count=0
            while read<n and current == chars[read]:
                count+=1
                read+=1
            chars[write]=current
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write

        
