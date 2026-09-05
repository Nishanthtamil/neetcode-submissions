class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo ={}
        def path(i,j):
            if i ==0 or j == 0:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            result = path(i-1,j) +path(i,j-1)
            memo[(i,j)] = result
            return result
        return path(m-1,n-1)