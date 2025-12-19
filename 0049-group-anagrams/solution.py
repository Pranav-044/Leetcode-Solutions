class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        dictionary=defaultdict(list)
        for s in strs:
            array=[0]*26
            for i in s:
                array[ord(i)-ord("a")]+=1
            dictionary[tuple(array)].append(s)
        return list(dictionary.values())
        
