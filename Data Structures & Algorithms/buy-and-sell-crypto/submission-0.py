class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpr=0
        minpr=prices[0]
        for sell in prices:
            maxpr=max(maxpr,sell-minpr)
            minpr=min(minpr,sell)
        return maxpr