class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        i=0
        n=len(s)
        z=float('-inf')
        while i<n:
            p=set()
            for j in range(i, n):
                if s[j] not in p:
                    p.add(s[j])
                    z=max(z,len(p))
                else:
                    break
            i += 1
        return int(z)