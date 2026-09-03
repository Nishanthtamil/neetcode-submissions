class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [0] * (len(nums))
        table[0] = nums[0]
        for i in range(1,len(nums)):
            table[i] = max(table[i-1],(nums[i]+table[i-2]))
        return table[len(nums)-1]