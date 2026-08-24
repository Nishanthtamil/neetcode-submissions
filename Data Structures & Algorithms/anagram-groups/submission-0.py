class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol={}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            if key in sol:
                sol[key].append(s)
            else:
                sol[key]=[s]
        return sol.values()