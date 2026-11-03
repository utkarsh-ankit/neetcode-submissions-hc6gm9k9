class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={i:s.count(i) for i in set(s)}
        b={j:t.count(j) for j in set(t)}
        return a==b
        