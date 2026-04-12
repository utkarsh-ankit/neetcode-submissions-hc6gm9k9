class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for i in strs:
            a="".join(sorted(i))
            if a not in groups:
                groups[a]=[]
            groups[a].append(i)
        return list(groups.values())

        #without sorting

