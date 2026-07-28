from typing import List

class MaxRainWater:
    def trap_water(self, heights: List[int]):
        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        maxLeft, maxRight = heights[l], heights[r]
        result = 0
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, heights[l])
                result += maxLeft - heights[l]
            else:
                r -= 1
                maxRight = max(maxRight, heights[r])
                result += maxRight - heights[r]
        return result