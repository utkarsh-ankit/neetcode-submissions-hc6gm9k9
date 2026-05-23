# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n=n
        c=0
        for i in range(1,n):
            if knows(c,i):
                c=i
        if self.is_celebrity(c):
            return c
        return -1

    def is_celebrity(self,i):
        for j in range(self.n):
            if i==j:
                continue
            if knows(i,j) or not knows(j,i):
                return False
        return True
        