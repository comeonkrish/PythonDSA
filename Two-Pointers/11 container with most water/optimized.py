class Solution:
    def maxArea(self, height) -> int:
        n = len(height)

        left = 0
        right = n - 1
        maxarea = 0

        while left < right:
            length = min(height[left], height[right])
            breadth = right - left
            temp_area = length*breadth

            if temp_area > maxarea:
                maxarea = temp_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea

obj = Solution()
ans = obj.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)
        