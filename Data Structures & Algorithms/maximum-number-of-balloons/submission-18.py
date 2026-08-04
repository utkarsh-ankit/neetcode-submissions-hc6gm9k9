from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon=Counter('balloon')
        # c=Counter(text)

        # res=float("inf")

        # for i in balloon:
        #     res=min(res,c[i]//balloon[i])
        # return res

        balloon=Counter("balloon")
        c=Counter(text)

        res=float("inf")

        for i in balloon:
            res=min(res,c[i]//balloon[i])
        return res

        