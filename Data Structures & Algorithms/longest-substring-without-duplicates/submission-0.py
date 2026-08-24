class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cont=set()
        left=0
        maxcont=0
        for right in range(len(s)):
            while s[right] in cont:
                cont.remove(s[left])
                left+=1
            cont.add(s[right])
            maxcont=max(maxcont,right-left+1)
        return maxcont