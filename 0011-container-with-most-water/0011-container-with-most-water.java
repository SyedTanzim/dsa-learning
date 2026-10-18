class Solution {
    public int maxArea(int[] height) {
        int maxWater = 0;

        int i = 0, j = height.length-1;

        while (i < j) {
            int len = j - i ;
            int water = 0;

            if (height[i] < height[j]) {
                water = height[i] * len;
                i++;
            }
            else if (height[i] == height[j]) {
                water = height[i] * len;
                i++;
                j--;
            } 
            else if (height[i] > height[j]) {
                water = height[j] * len;
                j--;
            }

            maxWater = Math.max(maxWater, water);
        }
        return maxWater;        
    }
}