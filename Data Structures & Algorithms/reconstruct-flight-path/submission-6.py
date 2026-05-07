class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj={s:[] for s, d in tickets}
        tickets.sort() #this will take care of the lexicographical ordering

        for s, d in tickets:
            adj[s].append(d)

        res=["JFK"]
        def dfs(s):
            if len(res)==len(tickets)+1:
                return True
            if s not in adj:
                return False

            temp=list(adj[s])
            for i, v in enumerate(temp):
                adj[s].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[s].insert(i,v)
                res.pop()
            return False

        dfs("JFK")
        return res





            
        