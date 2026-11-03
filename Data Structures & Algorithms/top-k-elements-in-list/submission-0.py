class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)

        pairs = list(counts.items())
        pairs.sort(key=lambda x: x[1])

        return [pairs[len(pairs)-i-1][0] for i in range(k)]
