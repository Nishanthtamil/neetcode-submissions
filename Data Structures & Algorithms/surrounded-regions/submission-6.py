class Solution:
    def solve(self, board: List[List[str]]) -> None:
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            stack=[(r,c)]
            while stack:
                r,c=stack.pop()
                if (r<0 or c<0 or r==rows or c==cols or board[r][c]!="O"):
                    continue
                board[r][c]="#"
                for dr,dc in direction:
                    stack.append((r+dr,c+dc))
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and 
                    (r in (0,rows-1) or c in (cols-1,0))):
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="#":
                    board[r][c]="O"