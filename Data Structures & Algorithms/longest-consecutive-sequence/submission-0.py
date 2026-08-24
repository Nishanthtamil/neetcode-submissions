class Solution:
    def longestConsecutive(self, nums: List[int]) :
        numset=set(nums)
        lcon=0
        for n in nums:
            if (n-1 not in numset):
                length=0
                while(n+length in numset):
                    length+=1
                lcon=max(length,lcon)
        return lcon