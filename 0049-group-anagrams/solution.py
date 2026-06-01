class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary=defaultdict(list)
        for i in strs:
            array=[0]*26
            for j in i:
                array[ord(j)-ord("a")]+=1
            dictionary[tuple(array)].append(i)
        return list(dictionary.values())

        
        























# dict1={}
#         dictionary=defaultdict(list)
#         for s in strs:
#             array=[0]*26
#             for i in s:
#                 array[ord(i)-ord("a")]+=1
#             dictionary[tuple(array)].append(s)
#         return list(dictionary.values())
