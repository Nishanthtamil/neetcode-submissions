class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0
        for num in num_set:
            if num-1 not in num_set:
                curr = num
                cur_streak = 1
                while curr+1 in num_set:
                    curr +=1
                    cur_streak+=1
                streak = max(cur_streak,streak)
        return streak