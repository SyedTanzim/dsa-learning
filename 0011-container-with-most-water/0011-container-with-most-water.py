class Solution:
    def maxArea(self, height: list[int]) -> int:
        totalWater = 0
        i = 0
        j = len(height) - 1

        while i <= j:
            water = 0
            totalLength = j - i

            if height[i] < height[j]:
                water = height[i] * totalLength
                if water > totalWater:
                    totalWater =  water
                i += 1
            elif height[i] > height[j]:
                water = height[j] * totalLength
                if water > totalWater:
                    totalWater =  water
                j -= 1
            else:
                water = height[i] * totalLength
                if water > totalWater:
                    totalWater =  water
                j -= 1
                i += 1

        return totalWater