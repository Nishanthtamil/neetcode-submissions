class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashm={i:[]for i in range(numCourses)}
        for pre,crs in prerequisites:
            hashm[pre].append(crs)
        visited=set()
        def dfs(c):
            if c in visited:
                return False
            if hashm[c]==[]:
                return True
            visited.add(c)
            for pre in hashm[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            hashm[c]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True