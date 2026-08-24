class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        cols=set()
        posdi=set()
        negdi=set()
        board=[["."] * n for row in range(n)]
        def dfs(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in cols or (r+c) in posdi or (r-c) in negdi:
                    continue
                cols.add(c)
                posdi.add(r+c)
                negdi.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                cols.remove(c)
                posdi.remove(r+c)
                negdi.remove(r-c)
                board[r][c]="."
        dfs(0)
        return res
