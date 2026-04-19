class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}

        for course, preq in prerequisites:
            adj[course].append(preq)

        vis=[0]*numCourses
        pathv=[0]*numCourses

        def dfs(node):
            vis[node]=1
            pathv[node]=1
            for preq in adj[node]:
                if not vis[preq]:
                    if dfs(preq):
                        return True
                elif pathv[preq]:
                    return True
            
            pathv[node]=0
            return False
            
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False
        return True