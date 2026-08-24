class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numin={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in numin:
                return [numin[diff],i]
            numin[num]=i