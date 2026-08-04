class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # result=[]

        # def backtrack(current,op,cl):
        #     if len(current)==2*n:
        #         result.append(current)

        #     if op<n:
        #         backtrack(current+"(",op+1,cl)
        #     if cl<op:
        #         backtrack(current+")",op,cl+1)

        # backtrack("",0,0)

        # return result

#---

        result=[]

        def backtrack(string,open,close):
            if len(string)==2*n:
                result.append(string)
            if open<n:
                backtrack(string+"(",open+1,close)
            if close<open:
                backtrack(string+")",open,close+1)
        backtrack("",0,0)
        return result














