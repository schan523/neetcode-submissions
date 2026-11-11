class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # where index i means the smallest value in prices up to index i
        smallest = [100] * len(prices)
        # where index i means the largest value starting from index i
        largest = [0] * len(prices)
        smallest[0] = prices[0] 
        largest[-1] = prices[-1]

        for i in range(1, len(prices)-1):
            smallest[i] = min(smallest[i-1], prices[i])
        for j in range(len(prices)-2, 0, -1):
            largest[j] = max(largest[j+1], prices[j])
        
        res = 0
        for k in range(len(prices)-1):
            res = max(res, largest[k+1]-smallest[k])
        
        return res if res > 0 else 0