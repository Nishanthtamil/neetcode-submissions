class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org=[]
        for i in nums :
            if i not in org:
                org.append(i)
            else :
                return True
        return False