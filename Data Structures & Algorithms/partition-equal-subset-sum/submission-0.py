class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextdp=set()
            for s in dp:
                if (s+nums[i])==target:
                    return True
                nextdp.add(s+nums[i])
                nextdp.add(s)
            dp=nextdp
        return True if target in dp else False