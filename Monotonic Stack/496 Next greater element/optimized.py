class Solution:
    def nextGreaterElement(self, nums1, nums2):

        next_greater = {}  # map of element -> next greater element in nums2
        stack = []  # Stack to keep track of elements from nums2 that need their next greater element

        for num in nums2:
            while stack and stack[-1] < num:
                print(stack[-1])
                next_greater[stack.pop()] = num

            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result

obj = Solution()

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
answer = obj.nextGreaterElement(nums1, nums2)
print(answer)  # Expected output: [-1, 3, -1]

# Additional test case: nums1 has only one element, and nums2 has no greater element for it
# nums1 = [2]
# nums2 = [1, 2, 3]
# answer = obj.nextGreaterElement(nums1, nums2)
# print(answer)  # Expected output: [3]

# # Additional test case: nums1 and nums2 have overlapping but non-matching elements
# nums1 = [2, 4]
# nums2 = [1, 2, 3, 4]
# answer = obj.nextGreaterElement(nums1, nums2)
# print(answer)  # Expected output: [3, -1]
