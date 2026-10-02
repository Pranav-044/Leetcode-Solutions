class MyHashMap:
    def __init__(self):
        self.arr=[[] for _ in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        found=False
        index=key%1000
        for i in range(len(self.arr[index])):
            if key == self.arr[index][i][0]:
                found = True
                self.arr[index][i][1] = value
        if not found: self.arr[index].append([key,value])
        

    def get(self, key: int) -> int:
        found=False
        index=key%1000
        for i in range(len(self.arr[index])):
            if(key == self.arr[index][i][0]):
                return self.arr[index][i][1]
        return -1

        

    def remove(self, key: int) -> None:
        index=key%1000
        for pair in self.arr[index]:
            if pair[0] == key:
                self.arr[index].remove(pair)
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)