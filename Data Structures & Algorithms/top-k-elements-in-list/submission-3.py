class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i , 0)
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt,num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res