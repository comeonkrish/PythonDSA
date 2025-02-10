class Solution:
    def maxArea(self, height) -> int:
        print(height)

        n = len(height)

        area = []

        for i in range(n):
            for j in range(i+1,n):
                length = min(height[i], height[j])
                breadth = j - i
                area.append(length*breadth)

        return area

obj = Solution()
ans = obj.maxArea([1,8,6,2,5,4,8,3,7])
# print(ans)
print(max(ans))
        