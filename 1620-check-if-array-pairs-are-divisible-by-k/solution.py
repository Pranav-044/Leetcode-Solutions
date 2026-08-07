class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dictionary={}
        for i in range(len(arr)):
            modulus=(arr[i]%k)
            if modulus not in dictionary:
                dictionary[modulus] = 0
            dictionary[modulus]+=1
        for (key,val) in dictionary.items():
            if(key == 0):
                print(dictionary[key])
                if(dictionary[key]%2!=0):
                    return False
                else:
                    continue
            elif key == (k-key):
                if(dictionary[key]%2 !=0):
                    return False
                else:
                    continue
            elif k-key not in dictionary:
                return False
            elif(dictionary[key] != dictionary[k-key]):
                
                return False
        return True 
        



        
