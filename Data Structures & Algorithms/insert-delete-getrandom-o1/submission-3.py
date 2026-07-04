import random

class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.dic={}
        

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        self.lst.append(val)
        self.dic[val]=len(self.lst)-1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        i=self.dic[val]

        last_val=self.lst[-1]
        self.dic[last_val]=i

        self.lst[i],self.lst[-1]=self.lst[-1],self.lst[i]
        
        self.lst.pop()
        del self.dic[val]

        return True

        

    def getRandom(self) -> int:
        random_index=random.randint(0,len(self.lst)-1)
        return self.lst[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()