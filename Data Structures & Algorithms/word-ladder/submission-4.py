from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        #neigs
        nei=collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)

        #bfs

        visit=set([beginWord])
        q=deque([beginWord])
        res=1

        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    p=word[:j]+"*"+word[j+1:]

                    for n in nei[p]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
            res+=1
        return 0





        
