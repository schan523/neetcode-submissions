class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        
        if len(s) < len(t):
            return ""

        counts = collections.Counter(t)
        curr = collections.defaultdict(int)
        
        left, right = 0, 0
        res = [-1, -1]
        have = 0
        while right < len(s):   
            curr[s[right]] += 1
            if counts[s[right]] and curr[s[right]] == counts[s[right]]:
                have += 1

            while have == len(counts):
                if res == [-1, -1]:
                    res = [left, right]
                else:
                    if res[1]-res[0] > right-left:
                        res = [left, right]
                curr[s[left]] -= 1
                if counts[s[left]] and curr[s[left]] < counts[s[left]]:
                    have -= 1
                left += 1
        
            right += 1

        return s[res[0]:res[1]+1]
