class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = {num: 1 for num in nums}

        res = 0
        for num in nums:
            if not n.get(num-1, False):
                i = num
                count = 1
                while n.get(i+1):
                    count += 1
                    i += 1
                res = max(res, count)
        
        return res