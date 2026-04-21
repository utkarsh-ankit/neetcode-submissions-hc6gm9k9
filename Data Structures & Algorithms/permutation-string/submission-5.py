class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count=Counter(s1)

        w=Counter(s2[:len(s1)])

        if w==s1_count:
            return True

        for i in range(len(s1), len(s2)):
            l=s2[i-len(s1)]
            r=s2[i]

            w[l]-=1
            if w[l]==0:
                del w[l]
            w[r]+=1

            if w==s1_count:
                return True
                
        return False

