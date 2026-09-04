class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decode(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            ans = decode(i+1)
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                ans+=decode(i+2)
                memo[i] = ans
            return ans

        return decode(0)