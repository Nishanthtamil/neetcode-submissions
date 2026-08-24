class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i not in unique:
                unique.add(i)
        return len(nums) != len(unique)