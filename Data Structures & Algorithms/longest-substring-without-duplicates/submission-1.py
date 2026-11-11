class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        
        counts = {}
        total = 1
        counts[s[0]] = 0
        threshold = -1

        for i, ch in enumerate(s):
            if i == 0:
                continue
            
            if counts.get(ch, -1) == -1 or (counts.get(ch, -1) != -1 and counts[ch] <= threshold):
                total = max(total, i - threshold)
                counts[ch] = i
            else:
                threshold = counts[ch]
                counts[ch] = i
        
        return total
