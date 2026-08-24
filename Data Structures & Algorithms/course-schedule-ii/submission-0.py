class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashm={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hashm[crs].append(pre)
        visit,cycle=set(),set()
        res=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in hashm[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res