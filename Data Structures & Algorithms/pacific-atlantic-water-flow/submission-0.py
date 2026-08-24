class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        pac,atl=set(),set()
        rows,cols=len(heights),len(heights[0])
        def dfs(r,c,isl,preheight):
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in isl or heights[r][c]<preheight):
                return
            isl.add((r,c)) 
            for dr,dc in direction:
                dfs(r+dr,c+dc,isl,heights[r][c])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res