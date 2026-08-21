from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied=defaultdict(int)
        for row,col in reservedSeats:
            if 1<col<10:
                occupied[row] |= (1<< col)
        count=(n-len(occupied))*2
        LEFT_MASK=(1<<2)|(1<<3)|(1<<4)|(1<<5)
        MIDDLE_MASK=(1<<4)| (1<<5)|(1<<6)|(1<<7)
        RIGHT_MASK=(1<<6)| (1<<7)|(1<<8)|(1<<9)
        for col in occupied.values():
            can_left=(LEFT_MASK & col) == 0
            can_right=(RIGHT_MASK & col) == 0
            can_middle=(MIDDLE_MASK & col) == 0
            if can_left and can_right:
                count+=2
            elif can_left or can_right or can_middle:
                count+=1
        return count


             


        # final=0
        # matrix={}
        # temp=0
        # count=0
        # visited=set()
        # for i,j in reservedSeats:
        #     if i not in matrix:
        #         matrix[i] = set()
        #     matrix[i].add(j)
        # for row,col in reservedSeats:
        #     if(row in visited):
        #         continue
        #     visited.add(row)
        #     v1,v2,v3=2,4,6
        #     check1=any(v1 in matrix[row] for v1 in range(v1,6))
        #     check2=any(v1 in matrix[row] for v1 in range(v2,8))
        #     check3=any(v1 in matrix[row] for v1 in range(v3,10))
        #     if(check1):
        #         if(check2 and not check3):
        #             count+=1
        #         elif(check3 and not check2):
        #             count+=1
        #         elif(not check2 and not check3):
        #             count+=1
        #     elif(check2):
        #         if(check1 and not check3):
        #             count+=1
        #         elif(check3 and not check1):
        #             count+=1
        #         elif(not check1 and not check3):
        #             count+=2
        #     elif(check3):
        #         if(check2 and not check1):
        #             count+=1
        #         elif(check2 and not check1):
        #             count+=1
        #         elif(not check1 and not check2):
        #             count+=1
        #     else:
        #         count+=2
        # count+=((n-len(matrix))*2)
        # return count

                






        
