class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque([nums[0]])

        for i in range(1, k):
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
        res = [d[0]] * (len(nums)-k+1)

        for i in range(k, len(nums)):
            if nums[i-k] == d[0]:
                d.popleft()
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
            res[i-k+1] = d[0]
        
        return res