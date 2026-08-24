class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bisect_left(la,a,lo=0,hi=None):
            if hi is None:
                hi=len(la)
            while lo<hi:
                mid=(lo+hi)//2
                if la[mid]<a:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        if not nums:
            return 0
        ta=[]
        for num in nums:
            index=bisect_left(ta,num)
            if index==len(ta):
                ta.append(num)
            else:
                ta[index]=num
        return len(ta)