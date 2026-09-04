class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        memo = {}
        def is_palin(i,j):
            if i>=j:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] != s[j]:
                memo[(i,j)] = False
            else:
                memo[(i,j)] = is_palin(i+1,j-1)
            return memo[(i,j)]

        start =0
        best =1 if s else 0
        for i in range(n):
            for j in range (i,n):
                if j-i+1 > best and is_palin(i,j):
                    start = i
                    best = j-i+1
        return s[start:start+best]