class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB=prices[0]
        maxP=0
        for sell in prices:
            maxP =max(maxP,sell-minB)
            minB = min(minB,sell)
        return maxP