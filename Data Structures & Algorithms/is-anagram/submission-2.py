class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS , sortedT = "".join(sorted(s)) , "".join(sorted(t))
        if len(s)!=len(t):
            return False
        for i in range (len(s)):
            if sortedS[i] != sortedT[i]:
                return False
        return True    