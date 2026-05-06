class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #check the boundary of the boeard fist and see the zeros, and do dfs on those, that will give us
        #the unsurrounded part first, then change them to "t". After that, just convert all the reming zeros of the boeard to x.
        #then cheange all the "t" back to zero. Reverse thinking.

        rows, cols=len(board), len(board[0])

        def dfs(r,c):
            if (r<0 or c<0 or c==cols or r==rows or board[r][c]!="O"):
                return
            board[r][c]="T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if (board[r][c]=="O" and (r in [0,rows-1] or c in [0, cols-1])):
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
        