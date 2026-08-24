class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<k:
            return []
        l=0
        maxar=[]
        for r in range(len(nums)):
            while k==(r-l+1):
                ar=nums[l:r+1]
                maxar.append(max(ar))
                l+=1
        return maxar