class Solution:
    def checkValidString(self, s: str) -> bool:
        # two pointers approach, we start from both end, if there is left and right  or star correspondigly
        # we weill move moth left nd right pointer inside, and if in the end there is a star or nothing, we return true, else false

        lmin,lmax=0,0

        for i in s:
            if i =="(":
                lmin+=1
                lmax+=1
            elif i==")":
                lmin-=1
                lmax-=1
            else:
                lmin-=1
                lmax+=1
            
            if lmax<0:
                return False

            if lmin<0:
                lmin=0

        return lmin==0
            
        