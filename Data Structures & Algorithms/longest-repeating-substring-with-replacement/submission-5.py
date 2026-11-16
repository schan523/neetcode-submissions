class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        left, right = 0, 0
        mostFreq = 0

        while right < len(s):
            counts[s[right]] += 1
            mostFreq = max(mostFreq, counts[s[right]])

            while (right-left+1 - mostFreq) > k:
                left += 1
                counts[s[left-1]] -= 1
            
            res = max(res, right-left+1)
            right += 1
        
        return res
