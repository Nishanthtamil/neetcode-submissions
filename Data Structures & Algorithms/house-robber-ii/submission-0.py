class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def lin(arr):
            prev,curr=0,0
            for num in arr:
                prev,curr=curr,max(curr,num+prev)
            return curr
        return max(lin(nums[:-1]),lin(nums[1:]))