class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        memo = {}
        def can_break(start):
            if start == n:
                return True
            if start in memo :
                return memo[start]
            for end in range(start+1,n+1):
                word = s[start:end]
                if word in words and can_break(end):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        return can_break(0)