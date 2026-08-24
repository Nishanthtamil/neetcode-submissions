class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        sort_items = sorted(freq.items(), key=lambda item:item[1] ,reverse=True)
        res = []
        for i in range(k):
            res.append(sort_items[i][0])
        return res 