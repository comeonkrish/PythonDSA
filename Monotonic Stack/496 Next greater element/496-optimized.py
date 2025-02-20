class Solution:
    def nextGreaterElement(self, nums1, nums2):

        next_greater_val = {}
        stack = []

        for num in nums2:

            while stack and num > stack[-1]:
                
                next_greater_val[stack.pop()] = num

            stack.append(num)

        while stack:
            next_greater_val[stack.pop()] = -1
        
        ans = [next_greater_val[num] for num in nums1]
        
        return ans


obj = Solution()
answer = obj.nextGreaterElement([4,1,2], [1,3,4,2])
print(answer)
        