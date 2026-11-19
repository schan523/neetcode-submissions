class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        opening = ["(", "{", "["]

        for ch in s:
            if ch in opening:
                queue.append(ch)
            else:
                if ch == ")" and (not queue or queue[-1] != "("):
                    return False
                elif ch == "}" and (not queue or queue[-1] != "{"):
                    return False
                elif ch == "]" and (not queue or queue[-1] != "["):
                    return False
                if queue:
                    queue.pop()

        return True if not queue else False