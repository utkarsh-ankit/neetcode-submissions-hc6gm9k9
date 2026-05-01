class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n=(n*10)+i
        n+=1
        return [int(j) for j in str(n)]
        