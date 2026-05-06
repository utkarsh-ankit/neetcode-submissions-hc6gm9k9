class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # rows, cols=len(heights), len(heights[0])
        # directions=[(1,0), (-1,0), (0,1), (0,-1)]

        # pacific=atlantic=False

        # def dfs(r,c, preval):
        #     nonlocal pacific, atlantic
        #     if r<0 or c<0:
        #         pacific=True
        #         return
        #     if r>=rows or c>=cols:
        #         atlantic=True
        #         return
        #     if heights[r][c]>preval:
        #         return

        #     tmp=heights[r][c]
        #     heights[r][c]=float("inf")
        #     for dx, dy in directions:
        #         dfs(r+dx, c+dy, tmp)
        #         if pacific and atlantic:
        #             break
        #     heights[r][c]=tmp

        # res=[]

        # for r in range(rows):
        #     for c in range(cols):
        #         pacific=False
        #         atlantic=False
        #         dfs(r,c, float('inf'))
        #         if pacific and atlantic:
        #             res.append([r,c])
        # return res

        rows, cols=len(heights), len(heights[0])
        pac, atl=set(), set()

        def dfs(r,c, visit, ph):
            if ((r,c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c]<ph):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r,cols-1, atl, heights[r][cols-1])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


        