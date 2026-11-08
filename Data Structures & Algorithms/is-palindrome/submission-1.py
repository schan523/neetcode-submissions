class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < len(s) and not s[start].isalnum():
            start += 1
        while end and not s[end].isalnum():
            end -= 1

        while start < end:
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
            while not s[start].isalnum():
                start += 1
            while not s[end].isalnum():
                end -= 1
        
        return True
