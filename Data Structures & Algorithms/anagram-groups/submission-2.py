class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups={}
        # for i in strs:
        #     a="".join(sorted(i))
        #     if a not in groups:
        #         groups[a]=[]
        #     groups[a].append(i)
        # return list(groups.values())

        #without sorting
        groups = {}
        
        for s in strs:
            # Create a count of 26 zeros (a-z)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple as key since lists can't be keys
            key = tuple(count)
            
            # Get the existing list for this key, or an empty one, then append
            groups[key] = groups.get(key, []) + [s]
            
        return list(groups.values())

