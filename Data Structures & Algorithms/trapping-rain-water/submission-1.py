class Solution:
    def trap(self, height: List[int]) -> int:
        peaks = []
        threshold = 0
        for i in range(len(height)):
            if height[i]:
                if not peaks:
                    threshold = height[i]
                while peaks and height[peaks[-1]] < height[i] and height[peaks[-1]] < threshold:
                    peaks.pop()
                if height[i] > threshold:
                    threshold = height[i]
                peaks.append(i)
        
        if not peaks or len(peaks) == 1:
            return 0
        
        total = 0
        left = peaks[0]
        for i in range(1, len(peaks)):
            h = min(height[left], height[peaks[i]])
            while left+1 < peaks[i]:
                left += 1
                total += (h - height[left])
            left = peaks[i]

        return total