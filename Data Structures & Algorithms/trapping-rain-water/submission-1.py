class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        l , r = 0, n - 1
        leftmax = height[l]
        rightmax = height[r]

        water = 0
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                water += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                water += rightmax - height[r]
        return water

        

           
            