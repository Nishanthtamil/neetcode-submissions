class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        un = set()
        for i in nums:
            if i in un:
                return True
            un.add(i)
        return False