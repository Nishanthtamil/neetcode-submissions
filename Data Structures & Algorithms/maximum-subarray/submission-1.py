class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMin,curMax= 0,0
        res = nums[0]
        for num in nums:
            tmp = curMax + num
            curMax = max(curMax+num , curMin + num,num)
            curMin = min(tmp , curMin + num , num)
            res = max(curMax,res)
        return res