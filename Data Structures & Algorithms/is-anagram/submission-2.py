class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        return set(s)==set(t) and len(s)==len(t)
        