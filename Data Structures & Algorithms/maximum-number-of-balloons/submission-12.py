from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon=Counter('balloon')
        # c_text=Counter(text)

        # res=float("inf")

        # for c in balloon:
        #     res=min(res,c_text[c]//balloon[c])
        # return res

        balloon=Counter('balloon')
        c=Counter(text)

        res=float("inf")

        for i in balloon:
            res=min(res,c[i]//balloon[i])
        return res

        