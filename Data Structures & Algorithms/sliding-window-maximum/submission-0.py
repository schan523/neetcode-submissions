class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = nums[:k]
        heapq.heapify_max(m)
        popped = defaultdict(int)
        
        res = [m[0]] * (len(nums)-k+1)
        for i in range(len(nums)-k):
            popped[nums[i]] += 1
            heapq.heappush_max(m, nums[i+k])
            while popped[m[0]]:
                num = heapq.heappop_max(m)
                popped[num] -= 1
            res[i+1] = m[0]

        
        return res