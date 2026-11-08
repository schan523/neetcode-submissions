class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bar1, bar2 = 0, len(heights)-1
        vol = (bar2 - bar1) * min(heights[bar1], heights[bar2])

        def calc(ind1, ind2):
            return (ind2 - ind1) * min(heights[ind1], heights[ind2])

        while bar1 < bar2:
            if heights[bar1] < heights[bar2]:
                temp = bar1+1
                while heights[temp] <= heights[bar1] and temp+1 < bar2:
                    temp += 1
                if heights[temp] > heights[bar1]:
                    vol = max(vol, calc(temp, bar2))
                    bar1 = temp
                else:
                    break
            elif heights[bar2] < heights[bar1]:
                temp = bar2-1
                while heights[temp] < heights[bar2] and temp > bar1:
                    temp -= 1
                if heights[temp] > heights[bar2]:
                    bar2 = temp
                    vol = max(vol, calc(bar1, bar2))
                else:
                    break
            else:
                temp1, temp2 = bar1+1, bar2-1
                while temp1+1 < temp2 and heights[temp1] <= heights[bar1]:
                    temp1 += 1
                while temp2-1 > temp1 and heights[temp2] <= heights[bar2]:
                    temp2 -= 1
                if temp1 >= temp2:
                    break

                bar1, bar2 = temp1, temp2
                vol = max(vol, calc(bar1, bar2))

        
        return vol