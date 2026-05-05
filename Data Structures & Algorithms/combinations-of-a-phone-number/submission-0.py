class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dc={
        "2":"abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        def backtrack(i, c):
            if len(c)==len(digits):
                res.append(c)
                return
            for j in dc[digits[i]]:
                backtrack(i+1, c+j)

        if digits:
            backtrack(0, "")

        return res


