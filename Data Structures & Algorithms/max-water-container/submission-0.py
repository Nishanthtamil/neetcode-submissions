class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        premaxwater=0
        while left<right:
            maxwater=min(heights[left],heights[right])*(right-left)
            premaxwater=max(premaxwater,maxwater)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return premaxwater