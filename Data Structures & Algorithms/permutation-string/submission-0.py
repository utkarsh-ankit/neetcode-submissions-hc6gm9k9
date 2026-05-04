class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count=Counter(s1)

        w=Counter(s2[:len(s1)])

        if w==s1_count:
            return True
        # l=0
        # r=len(s)
        for i in range(len(s1), len(s2)):
            if w==s1_count:
                return True
            else:
                w=Counter(s2[i:len(s1)+i])
        return False

