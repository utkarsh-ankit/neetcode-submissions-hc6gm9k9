class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(x,y,operator):
            if operator=="+":
                return x
            if operator=="-":
                return -x
            if operator=="*":
                return x*y
            return int(x/y)

        stack=[]
        curr=0
        pre_o="+"
        s+="@"

        for c in s:
            if c.isdigit():
                curr=curr*10+int(c)
            elif c=="(":
                stack.append(pre_o)
                pre_o="+"
            else:
                if pre_o in "*/":
                    stack.append(evaluate(stack.pop(),curr,pre_o))
                else:
                    stack.append(evaluate(curr,0,pre_o))

                curr=0
                pre_o=c
                if c==")":
                    while type(stack[-1])==int:
                        curr+=stack.pop()
                    pre_o=stack.pop()

        return sum(stack)


        