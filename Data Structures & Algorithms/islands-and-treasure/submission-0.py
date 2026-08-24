class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        rows,cols=len(grid),len(grid[0])
        dist=0
        visit=set()
        q=deque()
        def addrooms(r,c):
            if(r<0 or c<0 or r==rows or c==cols or (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                for dr,dc in direction:
                    addrooms(r+dr,c+dc)
            dist+=1
