class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        res = 1.0
        abs_n = abs(n)
        curr_x = x if n > 0 else 1/x
        
        for i in range(abs_n):
            res *= curr_x
            
        return res