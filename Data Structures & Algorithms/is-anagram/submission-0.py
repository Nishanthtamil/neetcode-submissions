class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        frqs,frqt={},{}
        for i in range(len(s)):
            frqs[s[i]]=1+frqs.get(s[i],0)
            frqt[t[i]]=1+frqt.get(t[i],0)
        return frqs==frqt