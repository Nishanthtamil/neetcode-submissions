class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol,mul=[],1
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if (i==j):
                    continue
                else:
                    mul*=nums[j]
            sol.append(mul)
        return sol