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


    # def generatep(n):
        # result=[]

        # def backtrack(string_,op,cl):
        #     if len(string_)==2*n:
        #         result.append(string_)
        #         return
        #     if op<n:
        #         backtrack(string_+"(", op+1, cl)
        #     if cl<op:
        #         backtrack(string_+")", op, cl+1)

        # backtrack("",0,0)

        # return string_

        result=[]

        def backtrack(string_,open,close):
            if len(string_)==2*n:
                result.append(string_)
                return
            if open<n:
                backtrack(string_+"(",open+1,close)
            if close<open:
                backtrack(string_+")",open,close+1)
            
        backtrack("",0,0)
        return result













