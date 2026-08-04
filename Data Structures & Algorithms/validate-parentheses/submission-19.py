class Solution:
    def isValid(self, s: str) -> bool:
        # stack=[]

        # a=["{","[","("]

        # for i in s:
        #     if i in a:
        #         stack.append(i)
        #     else:
        #         if i=="}":
        #             if stack and stack[-1]=="{":
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i=="]":
        #             if stack and stack[-1]=="[":
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif i==")":
        #             if stack and stack[-1]=="(":
        #                 stack.pop()
        #             else:
        #                 return False
        # return False if stack else True

        stack=[]
        a=["{","[","("]

        for i in s:
            if i in a:
                stack.append(i)
            else:
                if i==")":
                    if stack and stack[-1]=="(":
                        stack.pop()
                    else:
                        return False
                if i=="}":
                    if stack and stack[-1]=="{":
                        stack.pop()
                    else:
                        return False
                if i=="]":
                    if stack and stack[-1]=="[":
                        stack.pop()
                    else:
                        return False
        return False if stack else True

                
        