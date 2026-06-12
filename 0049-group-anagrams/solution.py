class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-ord("a")]+=1
            if tuple(arr) not in dictionary:
                dictionary[tuple(arr)]=[]    
            dictionary[tuple(arr)].append(i)    
                
        final=list(dictionary.values())
        return final    



        
        























# dict1={}
#         dictionary=defaultdict(list)
#         for s in strs:
#             array=[0]*26
#             for i in s:
#                 array[ord(i)-ord("a")]+=1
#             dictionary[tuple(array)].append(s)
#         return list(dictionary.values())
