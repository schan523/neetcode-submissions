import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = collections.Counter(s1)
        tempCounts = counts.copy()
        left = 0

        for i, right in enumerate(s2):
            while left+1 < len(s2) and not counts[s2[left]]:
                left += 1
            
            if i < left:
                continue

            if tempCounts[right]:
                tempCounts[right] -= 1
                if not tempCounts[right]:
                    del tempCounts[right]
                if not len(tempCounts):
                    return True
            else:
                while left < i and not tempCounts[right]:
                    left += 1
                    if counts[s2[left-1]]:
                        tempCounts[s2[left-1]] += 1
                if tempCounts[right]:
                    tempCounts[right] -= 1
                    del tempCounts[right]
                

        
        return False