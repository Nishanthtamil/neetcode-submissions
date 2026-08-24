class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        res=high
        while low<=high:
            middle=(low+high)//2
            totaltime=0
            for pile in piles:
                totaltime+=math.ceil(pile/middle)
            if totaltime<=h:
                res=middle
                high=middle-1
            else:
                low=middle+1
        return res